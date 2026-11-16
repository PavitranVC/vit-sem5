"""Build <subj>/patterns.json and <subj>/report.md from <subj>/analysis_raw.json (+ questions.csv, validation).
Usage: python -I _prep/analysis/tools/subject_patterns.py <subj>
Curated traps are tied to a real file:Qn and asserted to exist. Rubric elements come only from answer-key rows.
"""
import csv, json, re, sys, collections

S = sys.argv[1].lower()
B = f"_prep/analysis/{S}"
d = json.load(open(f"{B}/analysis_raw.json", encoding="utf-8"))
R = list(csv.DictReader(open(f"{B}/questions.csv", encoding="utf-8"), delimiter="|"))
bt = json.load(open("_prep/analysis/backtest_summary.json"))
VER = json.load(open(f"{B}/verification.json", encoding="utf-8"))
NAMES = {"dbs": "DBS (BCSE302L Database Systems)", "cn": "CN (BCSE308L Computer Networks)", "cd": "CD (BCSE307L Compiler Design)"}


def short(f):
    return f.split("/")[-1].replace(".pdf", "")


def cite(r):
    return f'{short(r["file_name"])}:Q{r["q_no"]}'


CITES = {cite(r) for r in R}
CUR = json.load(open(f"{B}/curated.json", encoding="utf-8")) if __import__("os").path.exists(f"{B}/curated.json") else {}
for t, items in CUR.get("traps", {}).items():
    for txt, c in items:
        assert c in CITES, f"bad cite {c}"

ts = d["topic_stats"]
core = d["core_code"]
ra = d["row_archetypes"]

# 2026-27 sister-course FAT signal and 2026-27 core CAT signal (observed)
sis26 = collections.defaultdict(set); cat26 = collections.defaultdict(set)
for r in R:
    a = ra.get(cite(r))
    if r["year"].startswith("2026") and r["exam"] == "FAT" and r["course_code"] != core:
        sis26[a].add(short(r["file_name"]))
    if r["year"].startswith("2026") and r["course_code"] == core and r["exam"] in ("CAT1", "CAT2"):
        cat26[a].add(short(r["file_name"]))
n_sis26 = len({f for v in sis26.values() for f in v}); n_cat26 = len({f for v in cat26.values() for f in v})

# answer-key rubric rows per topic
akby = collections.defaultdict(list)
for a in d["answer_key_rows"]:
    akby[a["arch"]].append(a)


def rubric(a):
    out = []
    for k in akby.get(a, [])[:2]:
        parts = []
        if k["step_marks"] and not k["step_marks"].startswith("not stated"):
            parts.append(f'marks: {k["step_marks"][:120]}')
        if k["required_keywords"]:
            parts.append(f'key shows: {k["required_keywords"][:160]}')
        if parts:
            out.append("; ".join(parts) + f' [{k["q"]}]')
    return out or None


def example(a):
    rows = [r for r in R if r["course_code"] == core and ra.get(cite(r)) == a and r["exam"] in ("FAT", "CAT1", "CAT2")]
    rows.sort(key=lambda r: (r["year"][:4], r["exam"] == "FAT"), reverse=True)
    if not rows:
        return None
    r = rows[0]
    return re.sub(r"\s*\[printed BL=\d\]", "", r["one_line_core_task"]) + f" (cite {cite(r)})"


order = [a for a in d["ranking"] if ts[a]["fat"]["k_recent"] + ts[a]["fat"]["k_older"] + ts[a]["all"]["k_recent"] + ts[a]["all"]["k_older"] > 0]
tier = lambda p: 1 if p >= 0.75 else (2 if p >= 0.5 else 3)
teach = sorted(order, key=lambda a: (tier(ts[a]["fat"]["probability"]), ts[a]["module"], order.index(a)))
topics = []
for i, a in enumerate(order, 1):
    st = ts[a]
    t = st["types"]
    topics.append({
        "rank": i, "teach_order": teach.index(a) + 1, "topic_name": a, "module": st["module"], "status": "observed",
        "probability": st["fat"]["probability"], "appearance_ratio": f'{st["fat"]["ratio"]} FATs',
        "recent_ratio": f'{st["fat"]["recent_ratio"]} FATs 2026-27',
        "probability_all_papers": st["all"]["probability"], "appearance_ratio_all_papers": f'{st["all"]["ratio"]} papers covering {st["module"]}',
        "recent_ratio_all_papers": f'{st["all"]["recent_ratio"]} 2026-27 papers',
        "sister_2026_27_fat_ratio": f"{len(sis26.get(a, []))} of {n_sis26}",
        "core_2026_27_cat_ratio": f"{len(cat26.get(a, []))} of {n_cat26}",
        "fat_mark_share": st["marks_share_fat"],
        "supporting_files": [c for c in st["support"] if "FAT" in c or "2026-2027" in c][:8] or st["support"][:8],
        "core_type": max(t, key=t.get) if t else None,
        "fluff_stripped_core_task": example(a),
        "observed_traps": [f"{x} [{c}]" for x, c in CUR.get("traps", {}).get(a, [])],
        "rubric_mandatory_elements": rubric(a),
        "worked_examples": [k["q"] for k in akby.get(a, [])][:4],
    })

sp = d["slot_pairs_pooled"]["rate"]
nfat = sum(1 for p in d["papers_core"].values() if p["exam"] == "FAT")
nfat_r = sum(1 for p in d["papers_core"].values() if p["exam"] == "FAT" and p["recent"])
meta = {"subject": NAMES.get(S, S), "student_slot": d["student_slot"],
        "probability_formula": f"probability = (2*k_recent + k_older + 1) / (2*n_recent + n_older + 2); k = papers containing the topic, n = papers; recent = 2026-27. Primary 'probability' uses {core} FAT papers only (n_recent={nfat_r}, n_older={nfat-nfat_r}). 'probability_all_papers' uses CAT1/CAT2/FAT papers whose measured syllabus window covers the topic's module ({d['coverage_windows']}).",
        "backtest_confidence": {"tier": bt["tier"], "hits": bt["hits"], "of": bt["of"]},
        "papers_used": len(d["papers_core"]), "tag_agreement_rate": VER["pooled_rate"],
        "tag_agreement_detail": VER["detail"],
        "small_n_warning": CUR.get("small_n_warning", "Probabilities are ranks from small samples, not calibrated chances."),
        "fat_blueprint_observed": CUR.get("blueprint", "")}
out = {"meta": meta, "predicted_topics": topics, "no_clear_pattern": CUR.get("no_clear_pattern", []),
       "slot_pair_hit_rates": {**{k: v for k, v in sp.items()}, "_n": f'{d["slot_pairs_pooled"]["n_questions"]} questions in {d["slot_pairs_pooled"]["n_pairs"]} slot pairs',
                               "_baseline_different_year_same_concept": d["different_year_pooled_null"]["rate"]["Same concept new numbers"],
                               "_cross_letter_same_year_same_concept": d["cross_letter_pooled"]["rate"]["Same concept new numbers"],
                               "_sister_courses_same_concept": d["sister_pooled"]["rate"]["Same concept new numbers"] if d["sister_pooled"]["n_questions"] else None}}
json.dump(out, open(f"{B}/patterns.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# ---------------- report.md ----------------
V = open(f"{B}/validation.md", encoding="utf-8").read()
nq = re.search(r"questions: (\d+)", V).group(1); nflag = V.count("| FLAG |"); nocr = re.search(r"ocr_flag=1: (\d+)", V).group(1)
L = [f"# {NAMES.get(S,S)}: FAT pattern report for slot {d['student_slot']}", "",
     "Machine-readable: `patterns.json`. Raw numbers: `analysis_raw.json`. Rows: `questions.csv`, `questions_text.jsonl`.",
     "**O** = observed (counted), **I** = inferred (rule or judgement). Every claim cites file:Qn.", "",
     "## 1. Data and validation", "", "| item | value |", "|---|---|",
     f"| question rows (all codes) | {nq} |",
     f"| distinct {core} papers (QP/AK duplicates merged by text similarity >= 0.6) | {len(d['papers_core'])}: {nfat} FAT ({nfat_r} from 2026-27), {sum(1 for p in d['papers_core'].values() if p['exam']=='CAT1')} CAT-1, {sum(1 for p in d['papers_core'].values() if p['exam']=='CAT2')} CAT-2 (O) |",
     f"| 2026-27 sister-course FATs | {n_sis26}: {', '.join(sorted({f for v in sis26.values() for f in v})) or 'none'} (O) |",
     f"| orchestrator re-read | {VER['detail']} (O) |",
     f"| marks check | {nflag} papers flagged (unprinted per-question marks, OR alternatives, case-study items); see validation.md (O) |",
     f"| rows with ocr_flag=1 | {nocr} (O) |",
     f"| backtest confidence (OS+AWS) | {bt['tier']}: {bt['hits']} of {bt['of']}; naive frequency list {bt['naive_hits']} of {bt['of']} (O) |", ""]
if CUR.get("blueprint"):
    L += ["## 2. FAT blueprint (O)", "", CUR["blueprint"], ""]
L += [f"## 3. Ranked topics for slot {d['student_slot']}", "",
      f"p = (2k_recent + k_older + 1)/(2n_recent + n_older + 2) over {core} FATs (n_recent={nfat_r}, n_older={nfat-nfat_r}). 'all' = CAT/FAT papers covering the module.", "",
      f"| rank | topic | mod | p (FAT) | FAT ratio | p (all) | all ratio | 2026-27 CATs (of {n_cat26}) | 2026-27 sister FATs (of {n_sis26}) | core type | example (fluff stripped) |",
      "|---|---|---|---|---|---|---|---|---|---|---|"]
for t in topics[:22]:
    ex = (t["fluff_stripped_core_task"] or "").replace("|", "/")
    L.append(f'| {t["rank"]} | {t["topic_name"]} | {t["module"]} | {t["probability"]:.2f} | {t["appearance_ratio"].replace(" FATs","")} | {t["probability_all_papers"]:.2f} | {t["appearance_ratio_all_papers"].split(" papers")[0]} | {t["core_2026_27_cat_ratio"].split(" of")[0]} | {t["sister_2026_27_fat_ratio"].split(" of")[0]} | {t["core_type"]} | {ex[:150]} |')
L += ["", "Teach order (I): tier p >= 0.75 by module, then 0.50-0.75, then the rest (`teach_order`).", ""]
L += ["## 4. Drift: 2026-27 vs older (O; small n)", "", "| exam | group | papers | mean Bloom | scenario wrapper % q | theory % marks | (num+trace):theory |", "|---|---|---|---|---|---|---|"]
for ex in ("CAT1", "CAT2", "FAT"):
    for g in ("older", "recent_2026_27"):
        s = d["drift"][ex][g]
        if s["n_q"]:
            L.append(f'| {ex} | {g} | {s["papers"]} | {s["mean_bloom"]} | {s["scenario_wrapper_pct_q"]} | {s["theory_marks_pct"]} | {s["num_trace_to_theory_mark_ratio"]} |')
L.append("| all | scenario wrapper % by start year | " + ", ".join(f'{y}: {s["scenario_wrapper_pct_q"]}' for y, s in d["drift"]["by_year_start"].items()) + " | | | | |")
L += ["", CUR.get("drift_note", ""), "", "## 5. Slot pairs and sister courses (I: rule-based matching)", "",
      "| comparison | n q | Identical | Same concept new numbers | Same module only | Unrelated |", "|---|---|---|---|---|---|"]
for lab, k in (("slot 1 -> slot 2, same exam+year", "slot_pairs_pooled"), ("different letter, same year", "cross_letter_pooled"),
               ("baseline: same exam, different year", "different_year_pooled_null"), ("sister course vs core, same exam+year", "sister_pooled")):
    p = d[k]
    if p["n_questions"]:
        r_ = p["rate"]; L.append(f'| {lab} ({p["n_pairs"]} pairs) | {p["n_questions"]} | {r_["Identical"]} | {r_["Same concept new numbers"]} | {r_["Same module only"]} | {r_["Unrelated"]} |')
L += ["", CUR.get("pairs_note", ""), "", "## 6. Answer keys: what earns marks (O)", "",
      f'{len(d["answer_key_rows"])} key rows; step marks stated in {sum(1 for a in d["answer_key_rows"] if a["step_marks"] and not a["step_marks"].startswith("not stated"))}; penalties stated in {sum(1 for a in d["answer_key_rows"] if a["penalties"] and not a["penalties"].startswith("not stated"))}.', "",
      "| topic | mandatory elements from real keys |", "|---|---|"]
for t in topics:
    if t["rubric_mandatory_elements"]:
        L.append(f'| {t["topic_name"]} | ' + "<br>".join(x.replace("|", "/") for x in t["rubric_mandatory_elements"]) + " |")
L += ["", "## 7. Observed traps", ""]
for t in topics:
    for x in t["observed_traps"]:
        L.append(f'- {t["topic_name"]}: {x}')
L += ["", "## 8. No clear pattern", ""] + [f"- {x}" for x in CUR.get("no_clear_pattern", [])]
L += ["", CUR.get("extra", "")]
open(f"{B}/report.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print(S, "patterns + report:", len(topics), "topics; top 8:", [t["topic_name"] for t in topics[:8]])
