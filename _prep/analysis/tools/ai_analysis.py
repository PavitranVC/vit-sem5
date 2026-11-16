"""Phase 2 analysis for AI (BCSE306L). Writes _prep/analysis/ai/analysis_raw.json.
Run from repo root: python -I _prep/analysis/tools/ai_analysis.py
All counts are 'observed'; archetype mapping and match categories are rule-based ('inferred').
"""
import csv, json, re, collections, difflib, itertools

BASE = "_prep/analysis/ai"
R = list(csv.DictReader(open(f"{BASE}/questions.csv", encoding="utf-8"), delimiter="|"))
TXT = {(j["file_name"], str(j["q_no"])): j for j in map(json.loads, open(f"{BASE}/questions_text.jsonl", encoding="utf-8"))}
for r in R:
    r["text"] = TXT.get((r["file_name"], r["q_no"]), {}).get("question_text") or ""

# --- archetypes: (id, label, module, regex on topic + core task) -------------------------------
ARCH = [
    ("INTRO", "AI foundations, history, types of AI", "M1", r"histor|approach|foundation|views? of ai|super ai|narrow|applications? of ai|ai applications|subfield|ai classification|AI views"),
    ("AGENT", "Agent types & architectures (reflex/model/goal/utility/learning, rationality)", "M1", r"agent type|reflex|goal-based|utility|learning agent|rational|agent architecture|model-based|agent type selection|route optimization agent|agents? \(five\)"),
    ("PEAS_ENV", "PEAS + task-environment properties", "M1", r"PEAS|environment|observab"),
    ("FORMULATION", "Problem formulation / state space (8-puzzle heuristics & parity, river crossing, water jug, Hanoi)", "M2", r"formulat|state space|water jug|hanoi|river|8-puzzle|8-queens state|soldiers"),
    ("UNINFORMED", "Uninformed search trace (BFS/DFS/DLS/IDS)", "M2", r"\bBFS\b|\bDFS\b|depth-limited|\bIDS\b|IDDFS|iterative deepening|uninformed|breadth|depth-first|depth first"),
    ("UCS", "Uniform cost search", "M2", r"\bUCS\b|uniform cost|uniform-cost"),
    ("INFORMED", "Informed search: Greedy best-first / A* / heuristics", "M2", r"A\*|greedy|best-first|best first|GBFS|heuristic admiss|heuristic under|15-puzzle"),
    ("LOCAL", "Hill climbing + simulated annealing", "M3", r"hill.?climb|simulated anneal|local maxim|plateau"),
    ("GA", "Genetic algorithm", "M3", r"genetic|\bGA\b"),
    ("ADVERSARIAL", "Minimax + alpha-beta pruning", "M3", r"minimax|mini-max|alpha|game tree"),
    ("FOL_REP", "English to FOL / CNF conversion", "M4", r"\bFOL\b|first.order|CNF|conjunctive normal|predicate|contrapositive"),
    ("RESOLUTION", "Resolution refutation proof (prop./FOL)", "M4", r"resolution|refutation|unification"),
    ("CHAINING", "Forward / backward chaining", "M4", r"chaining"),
    ("PROP_INF", "Propositional inference, truth tables, validity", "M4", r"propositional|truth table|tautolog|modus|validity|satisfiab|entailment|laws of inference|inference rules|logic puzzle"),
    ("KR", "Knowledge representation (frames, semantic nets, rules, expert systems)", "M4", r"frame|semantic net|rule-based|expert system|situation calculus"),
    ("BAYES", "Bayes' rule / conditional & total probability", "M5", r"bayes.? (theorem|rule)|conditional prob|probability laws|total probability|uncertainty|probabilistic (decision|clinical|reasoning)|expected return"),
    ("BAYESNET", "Bayesian network inference (joint / conditional from CPTs)", "M5", r"bayesian network|bayes net|joint prob|\bCPT|gibbs|\bHMM\b"),
    ("NAIVE_BAYES", "Naive Bayes classification", "M5", r"naive bayes"),
    ("PLANNING_STRIPS", "STRIPS / classical planning (blocks world, POP, planning graph)", "M6", r"STRIPS|partial.order|planning graph|blocks|planning \(forward|forward vs backward|forward and backward search|nondeterministic planning|planning types"),
    ("PLANNING_HTN", "Hierarchical (HTN) planning, multi-agent planning", "M6", r"hierarch|HTN|multi-robot|task network"),
    ("NLP_IR", "NLP, language models, information retrieval/extraction", "M7", r"NLP|language model|parsing|information retrieval|information extraction|retrieval/extraction|PageRank|search engine|communication"),
    ("VISION", "Perception / object recognition / image retrieval", "M7", r"object recognition|image retrieval|perception|vision"),
]
ML = r"PCA|regression|KNN|decision tree|confusion|feature engineering|missing value|data cleaning|fraud|clustering|k-means|neural|perceptron"


def archetypes(r):
    """Multi-label from the core task (specific); topic label only as fallback. Primary = core-task hit
    that also matches the topic label, else first core-task hit, else first topic hit."""
    task, topic = r["one_line_core_task"], r["topic"]
    t_hits = [a[0] for a in ARCH if re.search(a[3], task, re.I)]
    p_hits = [a[0] for a in ARCH if re.search(a[3], topic, re.I)]
    if re.search(ML, topic, re.I) or r["syllabus_module"].startswith("derived"):
        if not (t_hits or p_hits):
            return "ML_DERIVED", ["ML_DERIVED"]
    hits = t_hits or p_hits
    if not hits:
        m = r["syllabus_module"][:2]
        h = {"M6": "PLANNING_STRIPS", "M7": "NLP_IR"}.get(m, "OTHER_" + m)
        return h, [h]
    both = [h for h in t_hits if h in p_hits]
    prim = (both or t_hits or p_hits)[0]
    return prim, sorted(set(hits))


for r in R:
    r["arch_primary"], r["archs"] = archetypes(r)
    r["m"] = float(eval(r["marks"])) if re.fullmatch(r"[\d.+ ]+", r["marks"] or "") else None
    r["recent"] = r["year"].startswith("2026")

ALIASES = {"AI/PYQ/CAT1/BCSE306L-CAT-1-B1-2026-2027.pdf": "2026-27 QPs/AI/PYQ/BCSE306L/CAT1/BCSE306L-CAT1-B1-2026-2027-AK.pdf",
           "AI/PYQ/CAT1/BCSE306L-CAT1-C2-2025-2026-Key.pdf": "2026-27 QPs/AI/PYQ/BCSE306L/CAT1/BCSE306L-CAT1-C2-2026-2027.pdf"}
COVER = {"CAT1": {"M1", "M2", "M3"}, "CAT2": {"M3", "M4", "M5"}, "FAT": {f"M{i}" for i in range(1, 8)}}
ARCHMOD = {a[0]: a[2] for a in ARCH}
LABEL = {a[0]: a[1] for a in ARCH}

core = [r for r in R if r["course_code"] == "BCSE306L" and r["file_name"] not in ALIASES]
papers = collections.OrderedDict()
for r in core:
    papers.setdefault(r["file_name"], {"exam": r["exam"], "slot": r["slot"], "year": r["year"], "recent": r["recent"], "rows": []})["rows"].append(r)


def short(f):
    return f.split("/")[-1].replace(".pdf", "")


def cite(r):
    return f'{short(r["file_name"])}:Q{r["q_no"]}'


# --- (a) baseline + (f) probabilities ---------------------------------------------------------
def prob(kr, nr, ko, no):
    return (2 * kr + ko + 1) / (2 * nr + no + 2)


topic_stats = {}
for aid in list(LABEL):
    mod = ARCHMOD[aid]
    st = {"label": LABEL[aid], "module": mod}
    for scope, exams in [("fat", ["FAT"]), ("all", ["CAT1", "CAT2", "FAT"])]:
        elig = [(f, p) for f, p in papers.items() if p["exam"] in exams and mod in COVER[p["exam"]]]
        hit = [(f, p) for f, p in elig if any(aid in r["archs"] for r in p["rows"])]
        nr = sum(1 for _, p in elig if p["recent"]); no = len(elig) - nr
        kr = sum(1 for _, p in hit if p["recent"]); ko = len(hit) - kr
        st[scope] = {"k_recent": kr, "n_recent": nr, "k_older": ko, "n_older": no,
                     "ratio": f"{kr+ko} of {nr+no}", "recent_ratio": f"{kr} of {nr}", "older_ratio": f"{ko} of {no}",
                     "probability": round(prob(kr, nr, ko, no), 3)}
    rows = [r for r in core if aid in r["archs"]]
    st["support"] = [cite(r) for r in rows]
    st["marks_share_fat"] = round(sum(r["m"] or 0 for r in rows if r["exam"] == "FAT") /
                                  max(1, sum(r["m"] or 0 for r in core if r["exam"] == "FAT")), 3)
    st["types"] = dict(collections.Counter(r["type"] for r in rows))
    topic_stats[aid] = st

# --- (b) drift ----------------------------------------------------------------------------------
def style(rows):
    tm = sum(r["m"] or 0 for r in rows) or 1
    comp = sum(r["m"] or 0 for r in rows if r["type"] in ("numerical", "trace"))
    theo = sum(r["m"] or 0 for r in rows if r["type"] == "theory")
    scen_m = sum(r["m"] or 0 for r in rows if r["has_scenario_wrapper"] == "y")
    b = [int(r["bloom_level"]) for r in rows if r["bloom_level"].isdigit()]
    return {"n_q": len(rows), "marks": tm, "mean_bloom": round(sum(b) / max(1, len(b)), 2),
            "bloom_dist": dict(sorted(collections.Counter(b).items())),
            "scenario_wrapper_pct_q": round(100 * sum(r["has_scenario_wrapper"] == "y" for r in rows) / max(1, len(rows)), 1),
            "scenario_wrapper_pct_marks": round(100 * scen_m / tm, 1),
            "type_scenario_pct_q": round(100 * sum(r["type"] == "scenario" for r in rows) / max(1, len(rows)), 1),
            "computational_marks_pct": round(100 * comp / tm, 1), "theory_marks_pct": round(100 * theo / tm, 1),
            "num_trace_to_theory_mark_ratio": round(comp / theo, 2) if theo else None,
            "papers": len({r["file_name"] for r in rows})}


drift = {}
for ex in ["CAT1", "CAT2", "FAT", "ALL"]:
    rows = [r for r in core if ex == "ALL" or r["exam"] == ex]
    drift[ex] = {"older": style([r for r in rows if not r["recent"]]), "recent_2026_27": style([r for r in rows if r["recent"]])}
by_year = {}
for r in core:
    by_year.setdefault(r["year"][:4], []).append(r)
drift["by_year_start"] = {y: style(v) for y, v in sorted(by_year.items())}

# --- (c)(d) pair matching -----------------------------------------------------------------------
def norm(t):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t.lower())).strip()


def nums(t):
    return set(re.findall(r"\d+(?:\.\d+)?", t))


def classify(a, b):
    sim = difflib.SequenceMatcher(None, norm(a["text"]), norm(b["text"])).ratio() if a["text"] and b["text"] else 0
    na, nb = nums(a["text"]) - {"1", "2", "3", "4", "5", "10"}, nums(b["text"]) - {"1", "2", "3", "4", "5", "10"}
    numov = len(na & nb) / max(1, len(na | nb)) if (na or nb) else 1.0
    if sim >= 0.80 and numov >= 0.8:
        return 0, "Identical", round(sim, 2)
    if a["arch_primary"] == b["arch_primary"] or (set(a["archs"]) & set(b["archs"]) and sim >= 0.35):
        return 1, "Same concept new numbers", round(sim, 2)
    if a["syllabus_module"][:2] == b["syllabus_module"][:2]:
        return 2, "Same module only", round(sim, 2)
    return 3, "Unrelated", round(sim, 2)


CATS = ["Identical", "Same concept new numbers", "Same module only", "Unrelated"]


def compare(target_rows, source_rows):
    out = []
    for t in target_rows:
        best = min((classify(t, s) + (cite(s),) for s in source_rows), key=lambda x: (x[0], -x[2]))
        out.append({"q": cite(t), "marks": t["m"], "category": best[1], "best_match": best[3], "text_sim": best[2]})
    c = collections.Counter(o["category"] for o in out)
    mk = collections.defaultdict(float)
    for o in out:
        mk[o["category"]] += o["marks"] or 0
    tot = sum(mk.values()) or 1
    return {"by_question": {k: f"{c.get(k,0)} of {len(out)}" for k in CATS},
            "by_marks_pct": {k: round(100 * mk.get(k, 0) / tot, 1) for k in CATS}, "detail": out}


rows_of = collections.defaultdict(list)
for r in R:
    if r["file_name"] not in ALIASES:  # alias files are the same paper as their target; skip, never merge
        rows_of[r["file_name"]].append(r)
meta = {f: (rs[0]["course_code"], rs[0]["exam"], rs[0]["slot"], rs[0]["year"]) for f, rs in rows_of.items()}


def yr(y):
    return {"2023": "2023-2024", "2024": "2024-2025", "2025": "2025-2026?"}.get(y, y)


slot_pairs = []
for f1, f2 in itertools.permutations(meta, 2):
    c1, e1, s1, y1 = meta[f1]; c2, e2, s2, y2 = meta[f2]
    if c1 == c2 == "BCSE306L" and e1 == e2 and yr(y1) == yr(y2) and s1[0] == s2[0] and s1[1] == "1" and s2[1] == "2":
        slot_pairs.append({"pair": f"{e1} {s1}/{s2} {y1}", "slot1": short(f1), "slot2": short(f2), **compare(rows_of[f2], rows_of[f1])})

cross_letter = []  # same year+exam, different slot letter (e.g. B1 vs C2) - tells whether B1 FAT predicts C2 FAT
for f1, f2 in itertools.combinations(meta, 2):
    c1, e1, s1, y1 = meta[f1]; c2, e2, s2, y2 = meta[f2]
    if c1 == c2 == "BCSE306L" and e1 == e2 and yr(y1) == yr(y2) and s1[0] != s2[0]:
        cross_letter.append({"pair": f"{e1} {s1} vs {s2} {y1}", "source": short(f1), "target": short(f2), **compare(rows_of[f2], rows_of[f1])})

diff_year = []  # null baseline: same course+exam, different academic year
for f1, f2 in itertools.permutations(meta, 2):
    c1, e1, s1, y1 = meta[f1]; c2, e2, s2, y2 = meta[f2]
    if c1 == c2 == "BCSE306L" and e1 == e2 and yr(y1)[:4] != yr(y2)[:4]:
        diff_year.append(compare(rows_of[f2], rows_of[f1]))

sister_pairs = []
for f2, (c2, e2, s2, y2) in meta.items():
    if c2 == "BCSE306L":
        continue
    cands = [f for f, (c, e, s, y) in meta.items() if c == "BCSE306L" and e == e2 and yr(y) == yr(y2)]
    exact = [f for f in cands if meta[f][2] == s2]
    for f1 in (exact or cands):
        sister_pairs.append({"pair": f"{c2} {e2} {s2} {y2} vs BCSE306L {meta[f1][2]}", "same_slot": bool(exact),
                             "bcse": short(f1), "sister": short(f2), **compare(rows_of[f2], rows_of[f1])})


def pool(pairs):
    c = collections.Counter(); n = 0; mk = collections.defaultdict(float); tm = 0
    for p in pairs:
        for d in p["detail"]:
            c[d["category"]] += 1; n += 1; mk[d["category"]] += d["marks"] or 0; tm += d["marks"] or 0
    return {"n_questions": n, "n_pairs": len(pairs), "by_question": {k: f"{c.get(k,0)} of {n}" for k in CATS},
            "rate": {k: round(c.get(k, 0) / max(1, n), 3) for k in CATS},
            "by_marks_pct": {k: round(100 * mk.get(k, 0) / max(1, tm), 1) for k in CATS}}


# --- inter-agent consistency on the duplicated B1 CAT1 2026-27 paper ---------------------------
dupA = {r["q_no"]: r for r in R if r["file_name"] == "2026-27 QPs/AI/PYQ/BCSE306L/CAT1/BCSE306L-CAT1-B1-2026-2027-AK.pdf"}
dupB = {r["q_no"]: r for r in R if r["file_name"] == "AI/PYQ/CAT1/BCSE306L-CAT-1-B1-2026-2027.pdf"}
inter = {k: f'{sum(dupA[q][k] == dupB[q][k] for q in dupA if q in dupB)} of {len(set(dupA) & set(dupB))}'
         for k in ["type", "bloom_level", "has_scenario_wrapper", "marks", "syllabus_module"]}

# --- (e) answer keys ----------------------------------------------------------------------------
ak = []
for r in R:
    if r["course_code"] != "BCSE306L":
        continue
    if r["step_marks"] or r["required_keywords"]:
        if r["step_marks"] in ("", "not stated") and not r["required_keywords"]:
            continue
        ak.append({"q": cite(r), "arch": r["arch_primary"], "marks": r["marks"], "step_marks": r["step_marks"],
                   "required_keywords": r["required_keywords"], "penalties": r["penalties"],
                   "key_final_answer": r["key_final_answer"], "year": r["year"], "slot": r["slot"]})

# --- cross-year reuse: each 2026-27 BCSE306L question vs every older paper (any course) -----------
reuse = []
older_rows = [r for f, rs in rows_of.items() for r in rs if not rs[0]["year"].startswith("2026") and r["text"]]
for r in core:
    if not r["recent"] or not r["text"]:
        continue
    best = max(((difflib.SequenceMatcher(None, norm(r["text"]), norm(o["text"])).ratio(), o) for o in older_rows), key=lambda x: x[0])
    reuse.append({"q": cite(r), "best_older_match": cite(best[1]), "text_sim": round(best[0], 2),
                  "same_archetype": r["arch_primary"] == best[1]["arch_primary"]})
reuse.sort(key=lambda x: -x["text_sim"])

out = {"n_rows": len(R), "n_core_rows": len(core), "papers_core": {short(f): {k: v for k, v in p.items() if k != "rows"} for f, p in papers.items()},
       "topic_stats": topic_stats, "drift": drift, "slot_pairs": slot_pairs, "slot_pairs_pooled": pool(slot_pairs),
       "different_year_pooled_null": pool(diff_year), "cross_letter": cross_letter, "cross_letter_pooled": pool(cross_letter),
       "sister_pairs": sister_pairs, "sister_pooled": pool(sister_pairs),
       "sister_same_slot_pooled": pool([p for p in sister_pairs if p["same_slot"]]),
       "inter_agent_B1_CAT1_2026": inter, "reuse_2026_vs_older": reuse, "answer_key_rows": ak,
       "row_archetypes": {cite(r): [r["arch_primary"], r["archs"]] for r in R}}
json.dump(out, open(f"{BASE}/analysis_raw.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("ok", len(core), "core rows,", len(papers), "core papers,", len(slot_pairs), "slot pairs,",
      len(cross_letter), "cross-letter,", len(sister_pairs), "sister pairs,", len(ak), "AK rows")
