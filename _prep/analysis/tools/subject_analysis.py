"""Generic per-subject analysis (OS, AWS, DBS, CN, CD). Archetype = merged topic label.
Usage (repo root): python -I _prep/analysis/tools/subject_analysis.py <subj> <core_code> <student_slot|-> [backtest]
Writes _prep/analysis/<subj>/analysis_raw.json (and backtest.json when 'backtest' is given).
Counts are observed; topic merging, coverage windows and match categories are rule-based (inferred).
"""
import csv, json, re, sys, collections, difflib, itertools

SUBJ, CORE, SLOT = sys.argv[1].lower(), sys.argv[2], sys.argv[3]
DO_BT = len(sys.argv) > 4 and sys.argv[4] == "backtest"
B = f"_prep/analysis/{SUBJ}"
R = list(csv.DictReader(open(f"{B}/questions.csv", encoding="utf-8"), delimiter="|"))
TXT = {(j["file_name"], str(j["q_no"])): j for j in map(json.loads, open(f"{B}/questions_text.jsonl", encoding="utf-8"))}

MERGE = {  # regex on raw topic -> canonical label (first match wins); unmatched labels kept as-is
    "os": [(r"^OS (structure|functionalit|functions|design|abstractions)|monolithic|microkernel|clustered|multiprocessor", "OS structure / functions / types"),
           (r"test-and-set|mutex|critical section|bakery|peterson", "Critical section: Peterson / TSL / mutex / bakery"),
           (r"contiguous allocation", "Contiguous allocation (first/best/worst fit)"),
           (r"^IPC", "IPC"), (r"privileged|dual mode", "Dual mode / privileged instructions")],
    "aws": [(r"^Aurora|Aurora \+", "Aurora"), (r"DynamoDB", "DynamoDB"), (r"VPC peering|VPN|Direct Connect", "VPN / Direct Connect / VPC peering"),
            (r"SQS / SNS / Step", "SQS / SNS"), (r"^EC2 (instance|pricing|recovery)", "EC2 instance types / launch / pricing"),
            (r"EBS snapshots", "EBS vs EFS vs S3"), (r"Multi-region|global infrastructure", "Global infrastructure / multi-region DR"),
            (r"Glacier", "S3 storage classes / lifecycle"), (r"RDS vs DynamoDB", "RDS Multi-AZ / read replica")],
}.get(SUBJ, [])


def canon(t):
    for p, c in MERGE:
        if re.search(p, t, re.I):
            return c
    return t.strip() or "(blank)"


def num(x):
    try:
        return float(x)
    except Exception:
        return None


for r in R:
    r["text"] = (TXT.get((r["file_name"], r["q_no"])) or {}).get("question_text") or ""
    r["arch"] = canon(r["topic"])
    r["m"] = num(r["marks"])
    r["recent"] = r["year"].startswith("2026")
    r["mod"] = r["syllabus_module"][:2] if re.match(r"M\d", r["syllabus_module"]) else "derived"
    r["exam_n"] = r["exam"]  # ModelFAT (mock paper) stays separate and is not counted as a FAT


def norm(t):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t.lower())).strip()


def short(f):
    return f.split("/")[-1].replace(".pdf", "")


def cite(r):
    return f'{short(r["file_name"])}:Q{r["q_no"]}'


def yr(y):
    """Academic-year key. Bare years ('2024') are treated as the Fall of that year (= '2024-2025')."""
    m = re.match(r"(20\d\d)", y or "")
    return m.group(1) if m else ""


# QP/AK duplicates of the same paper: same course, exam, slot, year -> keep the file with most rows
groups = collections.defaultdict(list)
for f in {r["file_name"] for r in R}:
    rs = [r for r in R if r["file_name"] == f]
    groups[(rs[0]["course_code"], rs[0]["exam_n"], rs[0]["slot"], yr(rs[0]["year"]))].append((len(rs), f))
ALIAS = {}
for k, fs in groups.items():
    if k[1] in ("CASE",) or not k[2]:
        continue
    fs.sort(reverse=True)
    keep = fs[0][1]
    kt = " ".join(r["text"] for r in R if r["file_name"] == keep)[:3000]
    for _, f in fs[1:]:
        ft = " ".join(r["text"] for r in R if r["file_name"] == f)[:3000]
        if difflib.SequenceMatcher(None, norm(kt), norm(ft)).ratio() >= 0.6:  # same paper (QP vs AK); else keep both
            ALIAS[f] = keep

rows_of = collections.defaultdict(list)
for r in R:
    if r["file_name"] not in ALIAS:
        rows_of[r["file_name"]].append(r)
meta = {f: (rs[0]["course_code"], rs[0]["exam_n"], rs[0]["slot"], yr(rs[0]["year"]), rs[0]["recent"]) for f, rs in rows_of.items()}
core_files = [f for f, m in meta.items() if m[0] == CORE and m[1] in ("CAT1", "CAT2", "FAT")]

# coverage window per exam type, measured: modules with >=10% of that exam type's core rows
COVER = {}
for ex in ("CAT1", "CAT2", "FAT"):
    c = collections.Counter(r["mod"] for f in core_files if meta[f][1] == ex for r in rows_of[f])
    tot = sum(c.values()) or 1
    COVER[ex] = {m for m, n in c.items() if n / tot >= 0.10 and m != "derived"}
COVER["FAT"] = {r["mod"] for f in core_files for r in rows_of[f] if r["mod"] != "derived"}


def prob(kr, nr, ko, no):
    return (2 * kr + ko + 1) / (2 * nr + no + 2)


def topic_table(files):
    arch_mod = collections.Counter()
    for f in files:
        for r in rows_of[f]:
            arch_mod[(r["arch"], r["mod"])] += 1
    amod = {}
    for (a, m), n in arch_mod.most_common():
        amod.setdefault(a, m)
    out = {}
    for a, mod in amod.items():
        st = {"module": mod}
        for scope, exams in (("fat", ("FAT",)), ("all", ("CAT1", "CAT2", "FAT"))):
            elig = [f for f in files if meta[f][1] in exams and (mod in COVER[meta[f][1]] or meta[f][1] == "FAT")]
            hit = [f for f in elig if any(r["arch"] == a for r in rows_of[f])]
            nr = sum(meta[f][4] for f in elig); no = len(elig) - nr
            kr = sum(meta[f][4] for f in hit); ko = len(hit) - kr
            st[scope] = {"k_recent": kr, "n_recent": nr, "k_older": ko, "n_older": no, "ratio": f"{kr+ko} of {nr+no}",
                         "recent_ratio": f"{kr} of {nr}", "older_ratio": f"{ko} of {no}", "probability": round(prob(kr, nr, ko, no), 3)}
        rs = [r for f in files for r in rows_of[f] if r["arch"] == a]
        st["support"] = [cite(r) for r in rs]
        st["types"] = dict(collections.Counter(r["type"] for r in rs))
        fat_m = sum(r["m"] or 0 for f in files if meta[f][1] == "FAT" for r in rows_of[f])
        st["marks_share_fat"] = round(sum(r["m"] or 0 for r in rs if r["exam_n"] == "FAT") / max(1, fat_m), 3)
        out[a] = st
    return out


def rank(tt):
    return sorted(tt, key=lambda a: (-tt[a]["fat"]["probability"], -tt[a]["all"]["probability"], -tt[a]["marks_share_fat"]))


def style(rows):
    tm = sum(r["m"] or 0 for r in rows) or 1
    comp = sum(r["m"] or 0 for r in rows if r["type"] in ("numerical", "trace"))
    theo = sum(r["m"] or 0 for r in rows if r["type"] == "theory")
    b = [int(r["bloom_level"]) for r in rows if str(r["bloom_level"]).isdigit()]
    return {"papers": len({r["file_name"] for r in rows}), "n_q": len(rows), "mean_bloom": round(sum(b) / max(1, len(b)), 2),
            "scenario_wrapper_pct_q": round(100 * sum(r["has_scenario_wrapper"] == "y" for r in rows) / max(1, len(rows)), 1),
            "scenario_wrapper_pct_marks": round(100 * sum(r["m"] or 0 for r in rows if r["has_scenario_wrapper"] == "y") / tm, 1),
            "computational_marks_pct": round(100 * comp / tm, 1), "theory_marks_pct": round(100 * theo / tm, 1),
            "num_trace_to_theory_mark_ratio": round(comp / theo, 2) if theo else None}


def norm(t):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t.lower())).strip()


def nums(t):
    return set(re.findall(r"\d+(?:\.\d+)?", t)) - {"1", "2", "3", "4", "5", "10"}


CATS = ["Identical", "Same concept new numbers", "Same module only", "Unrelated"]


def classify(a, b):
    sim = difflib.SequenceMatcher(None, norm(a["text"]), norm(b["text"])).ratio() if a["text"] and b["text"] else 0
    na, nb = nums(a["text"]), nums(b["text"])
    numov = len(na & nb) / max(1, len(na | nb)) if (na or nb) else 1.0
    if sim >= 0.80 and numov >= 0.8:
        return 0, CATS[0], round(sim, 2)
    if a["arch"] == b["arch"]:
        return 1, CATS[1], round(sim, 2)
    if a["mod"] == b["mod"]:
        return 2, CATS[2], round(sim, 2)
    return 3, CATS[3], round(sim, 2)


def compare(tr, sr):
    out = []
    for t in tr:
        best = min((classify(t, s) + (cite(s),) for s in sr), key=lambda x: (x[0], -x[2]))
        out.append({"q": cite(t), "marks": t["m"], "category": best[1], "best_match": best[3], "text_sim": best[2]})
    c = collections.Counter(o["category"] for o in out)
    return {"by_question": {k: f"{c.get(k,0)} of {len(out)}" for k in CATS}, "detail": out}


def pool(pairs):
    c = collections.Counter(); n = 0
    for p in pairs:
        for d in p["detail"]:
            c[d["category"]] += 1; n += 1
    return {"n_questions": n, "n_pairs": len(pairs), "by_question": {k: f"{c.get(k,0)} of {n}" for k in CATS},
            "rate": {k: round(c.get(k, 0) / max(1, n), 3) for k in CATS}}


def pairs(pred):
    out = []
    for f1, f2 in itertools.permutations(meta, 2):
        if pred(meta[f1], meta[f2]):
            out.append({"pair": f"{meta[f1][1]} {meta[f1][2]}->{meta[f2][2]} {meta[f1][3]}", "source": short(f1), "target": short(f2),
                        **compare(rows_of[f2], rows_of[f1])})
    return out


same = lambda a, b: a[0] == b[0] == CORE and a[1] == b[1] and a[1] in ("CAT1", "CAT2", "FAT")
slot_pairs = pairs(lambda a, b: same(a, b) and a[3] == b[3] and a[2][:1] == b[2][:1] and a[2][1:] == "1" and b[2][1:] == "2")
cross = pairs(lambda a, b: same(a, b) and a[3] == b[3] and a[2][:1] < b[2][:1])
diffyr = pairs(lambda a, b: same(a, b) and a[3] != b[3])
sister = []
for f2, m2 in meta.items():
    if m2[0] == CORE or m2[1] not in ("CAT1", "CAT2", "FAT"):
        continue
    cands = [f for f in core_files if meta[f][1] == m2[1] and meta[f][3] == m2[3]]
    exact = [f for f in cands if meta[f][2] == m2[2]]
    for f1 in (exact or cands):
        sister.append({"pair": f"{m2[0]} {m2[1]} {m2[2]} {m2[3]} vs {CORE} {meta[f1][2]}", "same_slot": bool(exact),
                       "source": short(f1), "target": short(f2), **compare(rows_of[f2], rows_of[f1])})

core_rows = [r for f in core_files for r in rows_of[f]]
drift = {ex: {"older": style([r for r in core_rows if r["exam_n"] == ex and not r["recent"]]),
              "recent_2026_27": style([r for r in core_rows if r["exam_n"] == ex and r["recent"]])} for ex in ("CAT1", "CAT2", "FAT")}
drift["by_year_start"] = {y: style([r for r in core_rows if yr(r["year"]) == y]) for y in sorted({yr(r["year"]) for r in core_rows})}

older_rows = [r for f, rs in rows_of.items() if not meta[f][4] for r in rs if r["text"]]
reuse = []
for r in core_rows:
    if r["recent"] and r["text"] and older_rows:
        s, o = max(((difflib.SequenceMatcher(None, norm(r["text"]), norm(o["text"])).ratio(), o) for o in older_rows), key=lambda x: x[0])
        reuse.append({"q": cite(r), "best_older_match": cite(o), "text_sim": round(s, 2)})
reuse.sort(key=lambda x: -x["text_sim"])

ak = [{"q": cite(r), "arch": r["arch"], "marks": r["marks"], "step_marks": r["step_marks"], "required_keywords": r["required_keywords"],
       "penalties": r["penalties"], "key_final_answer": r["key_final_answer"]}
      for r in R if r["course_code"] == CORE and (r["required_keywords"] or (r["step_marks"] and r["step_marks"] != "not stated"))]

tt = topic_table(core_files)
out = {"subject": SUBJ, "core_code": CORE, "student_slot": SLOT, "coverage_windows": {k: sorted(v) for k, v in COVER.items()},
       "aliases_merged": {short(k): short(v) for k, v in ALIAS.items()},
       "papers_core": {short(f): {"exam": meta[f][1], "slot": meta[f][2], "year": meta[f][3], "recent": meta[f][4], "n_q": len(rows_of[f])} for f in core_files},
       "topic_stats": tt, "ranking": rank(tt), "drift": drift,
       "slot_pairs": slot_pairs, "slot_pairs_pooled": pool(slot_pairs), "cross_letter_pooled": pool(cross),
       "different_year_pooled_null": pool(diffyr), "sister_pairs": sister, "sister_pooled": pool(sister),
       "reuse_recent_vs_older": reuse[:40], "answer_key_rows": ak,
       "row_archetypes": {cite(r): r["arch"] for r in R}}

if DO_BT:
    # Predict each 2026-27 slot-2 FAT from: pre-2026-27 papers + 2026-27 CATs + the same-letter 2026-27 slot-1 FAT.
    bt = []
    recent_fats = {meta[f][2]: f for f in core_files if meta[f][1] == "FAT" and meta[f][4]}
    for s2, target in sorted(recent_fats.items()):
        if not s2.endswith("2") or s2[0] + "1" not in recent_fats:
            continue
        train = [f for f in core_files if not meta[f][4] or meta[f][1] != "FAT" or f == recent_fats[s2[0] + "1"]]
        t2 = topic_table(train)
        top = rank(t2)[:10]
        actual = {r["arch"] for r in rows_of[target]}
        hits = [a for a in top if a in actual]
        # naive baseline: 10 most frequent topics among pre-2026-27 FATs only
        old = collections.Counter(a for f in core_files if meta[f][1] == "FAT" and not meta[f][4] for a in {r["arch"] for r in rows_of[f]})
        naive = [a for a, _ in old.most_common(10)]
        slot1 = {r["arch"] for r in rows_of[recent_fats[s2[0] + "1"]]}
        bt.append({"target": short(target), "slot1_used": short(recent_fats[s2[0] + "1"]), "train_papers": len(train),
                   "predicted_top10": [{"topic": a, "p": t2[a]["fat"]["probability"], "ratio": t2[a]["fat"]["ratio"], "hit": a in actual} for a in top],
                   "hits": len(hits), "of": 10, "precision": f"{len(hits)} of 10",
                   "recall": f"{len(set(top) & actual)} of {len(actual)} distinct target topics",
                   "naive_older_fat_top10_hits": f"{len(set(naive) & actual)} of 10",
                   "slot1_topic_overlap": f"{len(slot1 & actual)} of {len(actual)} target topics also in slot-1 FAT",
                   "missed_target_topics": sorted(actual - set(top))})
    json.dump(bt, open(f"{B}/backtest.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    out["backtest"] = bt

json.dump(out, open(f"{B}/analysis_raw.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(SUBJ, "core papers", len(core_files), "| topics", len(tt), "| slot pairs", len(slot_pairs), "| sister pairs", len(sister),
      "| AK rows", len(ak), "| coverage", {k: sorted(v) for k, v in COVER.items()})
