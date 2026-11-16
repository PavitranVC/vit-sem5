"""Build _prep/analysis/ai/patterns.json from analysis_raw.json + questions.csv.
Curated traps/rubric elements are each tied to a real file:Qn (checked against questions.csv / key fields).
Run: python -I _prep/analysis/tools/ai_patterns.py [backtest_tier hits of]
"""
import csv, json, sys, re

B = "_prep/analysis/ai"
d = json.load(open(f"{B}/analysis_raw.json", encoding="utf-8"))
R = list(csv.DictReader(open(f"{B}/questions.csv", encoding="utf-8"), delimiter="|"))
ver = json.load(open(f"{B}/verification.json", encoding="utf-8")) if False else None


def short(f):
    return f.split("/")[-1].replace(".pdf", "")


CITES = {f'{short(r["file_name"])}:Q{r["q_no"]}' for r in R}

TRAPS = {
    "UNINFORMED": [("Ties broken alphabetically; in graph search a state is expanded only once (repeated states skipped).", "BCSE306L-FAT-B1-2026-2027:Q4"),
                   ("DFS can oscillate between two nodes (b-d-b-d); the key expects the loop to be noticed and BFS preferred.", "BCSE306L-CAT-1-B2-2023-2024:Q3"),
                   ("IDS restarts from the root at every depth limit; keys list the order for each iteration separately.", "BCSE306L-CAT1-D2-2025-2026-AK:Q3")],
    "INFORMED": [("A node can appear without a printed h value (node C has no h); state your assumption explicitly.", "BCSE306L-FAT-B1-2026-2027:Q4"),
                 ("Two heuristics compared: decide admissibility by comparing h with true cost h*.", "BCSE306L-CAT1-D1-2025-2026-AK:Q4b"),
                 ("15-puzzle A*: full solve is too long; key accepted following the A* flow with partial credit.", "BCSE306L-CAT1-D2-2025-2026-AK:Q4")],
    "UCS": [("Goal test happens when the goal is dequeued, not when generated; two paths can tie at the optimal cost (both cost 7).", "BCSE306L-CAT1-C2-2025-2026-Key:Q3a"),
            ("Equal-cost frontier entries resolved alphabetically.", "BCSE306L-CAT-1-B2-2023-2024:Q4"),
            ("Both the traversed (expansion) path and the actual solution path are asked.", "BCSE306L-CAT-1-E2-2024-2025:Q3b")],
    "ADVERSARIAL": [("Root can be a MIN node ('Assume min takes the first call').", "BCSE306L - Artificial Intelligence - CAT-2 - Slot E2 - 2024 - Question Paper:Q1"),
                    ("Pruned set changes with expansion order: left-to-right and right-to-left asked as separate parts.", "BCSE306L-CAT2-D1-2025-2026-AK:Q1iii")],
    "LOCAL": [("Asked whether hill climbing actually reaches the goal; answer from neighbour h values (it may stall).", "BCSE306L-FAT-B1-2026-2027:Q5c"),
              ("Simulated annealing needs the acceptance formula with a numeric example (e^(-5/20)=0.779).", "BCSE306L-CAT1-C2-2025-2026-Key:Q5b")],
    "FORMULATION": [("8-puzzle: inversion count ignores the blank; parity decides reachability before any moves.", "BCSE306L-FAT-B1-2026-2027:Q3")],
    "FOL_REP": [("'Exactly one' / 'only one' needs a uniqueness clause, not just an existential.", "BCSE306L - Artificial Intelligence - CAT-2 - Slot E2 - 2024 - Question Paper:Q3A")],
    "RESOLUTION": [("Negate the goal and add it to the clause set before resolving; keys show the unifier at each step down to the empty clause.", "BCSE306L - Artificial Intelligence - CAT-2 - Slot B1 - 2023 - Answer Key:Q2")],
    "PEAS_ENV": [("A drone operating in a cooperative fleet is multi-agent; all SIX dimensions need a one-sentence justification each.", "BCSE306L-CAT1-C2-2026-2027:Q2b")],
    "AGENT": [("Scoring routes (penalise tolls, reward speed) means utility-based, not goal-based.", "BCSE306L-CAT1-C2-2025-2026-Key:Q1a")],
    "BAYESNET": [("Joint probability includes negated variables (~B, ~E): use 1-P from the CPT.", "BCSE306L-FAT-B1-2026-2027:Q9a")],
    "NAIVE_BAYES": [("A zero conditional count makes the class score 0 (key shows P(Male,Fatigue,Cough|COVID-19)=0).", "BCSE306L - Artificial Intelligence - CAT-2 - Slot E1 - 2024 - Answer Key:Q5")],
    "CHAINING": [("A rule whose premise is unknown does not fire; keys note 'R2 not triggered'.", "BCSE306L - Artificial Intelligence - CAT-2 - Slot E1 - 2024 - Answer Key:Q3")],
}
RUBRIC = {
    "UNINFORMED": [("Pop/expansion order per algorithm; 3 marks per algorithm (1.5 stack/queue + 1.5 traversal)", "BCSE306L-CAT-1-B1-2023-2024:Q3a"),
                   ("Completeness, optimality, time and space for each algorithm", "BCSE306L-CAT-1-B1-2023-2024:Q3b")],
    "UCS": [("Priority queue + visited per step (4), search tree per step (3), path and cost of each goal (2), minimum-cost goal (1)", "BCSE306L-CAT-1-B2-2023-2024:Q4"),
            ("Frontier with g values after every expansion; goal test at dequeue", "BCSE306L-CAT1-C2-2025-2026-Key:Q3a")],
    "INFORMED": [("Table: path to state expanded, path length, total estimated cost f=g+h, expanded list", "BCSE306L-CAT1-B1-2026-2027-AK:Q5"),
                 ("f(n)=g(n)+h(n) per node; path and cost per heuristic; admissibility vs h*", "BCSE306L-CAT1-D1-2025-2026-AK:Q4a")],
    "ADVERSARIAL": [("Backed-up value of every internal node and the chosen root move", "BCSE306L-CAT2-D1-2025-2026-AK:Q1i"),
                    ("List of pruned nodes with the alpha/beta values at each prune", "BCSE306L-CAT2-D1-2025-2026-AK:Q1ii")],
    "LOCAL": [("Algorithm (1.5) + why hill climbing fails (2); algorithm (1.5) + why simulated annealing succeeds (2)", "BCSE306L-CAT1-D1-2025-2026-AK:Q5"),
              ("Local maximum, plateau/shoulder, ridge named with a labelled landscape diagram", "BCSE306L-CAT1-C2-2025-2026-Key:Q5a"),
              ("P = exp(deltaV/T) and a cooling schedule T(k+1) = alpha*T(k)", "BCSE306L-CAT1-C2-2025-2026-Key:Q5b")],
    "GA": [("Chromosome design, initialisation, fitness, selection, crossover, mutation, repeat", "BCSE306L-CAT1-D2-2025-2026-AK:Q5"),
           ("Encoding example and fitness function (8-queens: non-attacking pairs)", "BCSE306L-CAT-1-B1-2023-2024:Q5")],
    "PEAS_ENV": [("4 PEAS components (4) + environment classification (3) + agent architecture diagram with justification (3)", "BCSE306L-CAT1-D1-2025-2026-AK:Q1"),
                 ("2.5 marks per agent: observable, agents, deterministic, episodic, static, discrete", "BCSE306L-CAT-1-B1-2023-2024:Q2")],
    "AGENT": [("Diagram (2) + explanation (3)", "BCSE306L-CAT1-D1-2025-2026-AK:Q2a"),
              ("Name the agent type and justify from cues in the scenario", "BCSE306L-CAT1-C2-2025-2026-Key:Q1a")],
    "FOL_REP": [("Eliminate implication, De Morgan, distribution when converting to CNF", "BCSE306L - Artificial Intelligence - CAT-2 - Slot B1 - 2023 - Answer Key:Q3c")],
    "RESOLUTION": [("Predicate form, clause form, negated goal, unifiers, empty clause", "BCSE306L - Artificial Intelligence - CAT-2 - Slot B1 - 2023 - Answer Key:Q2"),
                   ("CNF clauses listed and numbered, negated goal, derivation to empty clause", "BCSE306L - Artificial Intelligence - CAT-2 - Slot B2 - 2023 - Answer Key:Q5a")],
    "CHAINING": [("Forward: rules fired in order with each new fact (A6, A7, ...); backward: goal-driven rule chain", "BCSE306L - Artificial Intelligence - CAT-2 - Slot B2 - 2023 - Answer Key:Q3a")],
    "PROP_INF": [("Classify each formula as valid / satisfiable / unsatisfiable", "BCSE306L-CAT2-D1-2025-2026-AK:Q2b"),
                 ("Name the inference rule used at each step (Modus Ponens, conjunction introduction)", "BCSE306L-CAT2-D2-2025-2026-AK:Q3B")],
    "NAIVE_BAYES": [("Priors, per-class product of conditionals, compare classes", "BCSE306L - Artificial Intelligence - CAT-2 - Slot B1 - 2023 - Answer Key:Q5")],
    "BAYESNET": [("Factorise the joint as a product of CPT entries; sum out hidden variables", "BCSE306L-CAT2-D1-2025-2026-AK:Q5")],
    "BAYES": [("Bayes formula with total probability in the denominator, numeric result", "BCSE306L-CAT2-D2-2025-2026-AK:Q4A")],
    "FORMULATION": [("Initial state, state space, actions, goal test, path cost", "BCSE306L-CAT1-B1-2026-2027-AK:Q4b")],
    "INTRO": [("Four approaches (thinking/acting humanly/rationally, Turing test) (2) + timeline (3)", "BCSE306L-CAT-1-B1-2023-2024:Q1a")],
}
for k, v in list(TRAPS.items()) + list(RUBRIC.items()):
    for _, c in v:
        assert c in CITES, f"bad cite {c}"

CORE_TYPE = {}
ts = d["topic_stats"]
for aid, st in ts.items():
    t = st["types"]
    CORE_TYPE[aid] = max(t, key=t.get) if t else "theory"


def example_task(aid):
    """Most recent FAT question for the archetype, else most recent any paper."""
    rows = [r for r in R if r["course_code"] == "BCSE306L" and aid in d["row_archetypes"].get(f'{short(r["file_name"])}:Q{r["q_no"]}', [None, []])[1]]
    rows.sort(key=lambda r: (r["exam"] == "FAT", r["year"][:4]), reverse=True)
    if not rows:
        return None
    r = rows[0]
    t = re.sub(r"\s*\[printed BL=\d\]", "", r["one_line_core_task"])
    return f'{t} (cite {short(r["file_name"])}:Q{r["q_no"]})'


def worked(aid):
    ak = [a["q"] for a in d["answer_key_rows"] if a["arch"] == aid]
    return ak[:4]


order = sorted(ts, key=lambda a: (-ts[a]["fat"]["probability"], -ts[a]["all"]["probability"], -ts[a]["marks_share_fat"]))
order = [a for a in order if ts[a]["fat"]["k_recent"] + ts[a]["fat"]["k_older"] + ts[a]["all"]["k_recent"] + ts[a]["all"]["k_older"] > 0]
tier = lambda p: 1 if p >= 0.75 else (2 if p >= 0.55 else 3)
teach = sorted(order, key=lambda a: (tier(ts[a]["fat"]["probability"]), ts[a]["module"], order.index(a)))

topics = []
for i, a in enumerate(order, 1):
    st = ts[a]
    sup = [c for c in st["support"] if "FAT" in c or "2026-2027" in c or "C2-2025-2026-Key" in c][:8] or st["support"][:8]
    topics.append({
        "rank": i, "teach_order": teach.index(a) + 1, "topic_id": a, "topic_name": st["label"], "module": st["module"],
        "status": "observed",
        "probability": st["fat"]["probability"],
        "appearance_ratio": f'{st["fat"]["ratio"]} FATs',
        "recent_ratio": f'{st["fat"]["recent_ratio"]} FATs 2026-27',
        "probability_all_papers": st["all"]["probability"],
        "appearance_ratio_all_papers": f'{st["all"]["ratio"]} papers whose syllabus window covers {st["module"]}',
        "recent_ratio_all_papers": f'{st["all"]["recent_ratio"]} 2026-27 papers',
        "fat_mark_share": st["marks_share_fat"],
        "supporting_files": sup,
        "core_type": CORE_TYPE[a],
        "fluff_stripped_core_task": example_task(a),
        "observed_traps": [f"{t} [{c}]" for t, c in TRAPS.get(a, [])],
        "rubric_mandatory_elements": [f"{t} [{c}]" for t, c in RUBRIC.get(a, [])] or None,
        "worked_examples": worked(a),
    })

bt = {"tier": "pending (Phase 3)", "hits": None, "of": None}
if len(sys.argv) == 4:
    bt = {"tier": sys.argv[1], "hits": int(sys.argv[2]), "of": int(sys.argv[3])}

sp = d["slot_pairs_pooled"]["rate"]
out = {
    "meta": {
        "subject": "AI (BCSE306L Artificial Intelligence)", "student_slot": "C2",
        "probability_formula": "probability = (2*k_recent + k_older + 1) / (2*n_recent + n_older + 2); k = papers containing the topic, n = papers; recent = 2026-27. Primary 'probability' uses BCSE306L FAT papers only (n_recent=1, n_older=6). 'probability_all_papers' uses CAT1/CAT2/FAT papers whose syllabus window covers the topic's module (CAT1=M1-M3, CAT2=M3-M5, FAT=M1-M7; observed).",
        "backtest_confidence": bt,
        "papers_used": len(d["papers_core"]),
        "papers_used_detail": "25 distinct BCSE306L papers (7 FAT, 11 CAT1, 7 CAT2) after merging QP/AK duplicates; sister-course papers (BITE308L, BECE309L, CSI3003) used only for sister comparison",
        "tag_agreement_rate": 0.886,
        "tag_agreement_detail": "orchestrator re-read of 35/344 questions: type 30/35, bloom 30/35, scenario wrapper 33/35, text 34/35",
        "small_n_warning": "Only one 2026-27 FAT (B1) exists, so 'recent' FAT evidence is a single paper. Treat probabilities as ranks, not calibrated chances.",
        "fat_blueprint_observed": "10 questions x 10 marks; all 7 modules in 7 of 7 FATs; typical order Q1 M1, Q2-Q3 M2, Q4-Q5 M3, Q5-Q7 M4, Q7-Q8 M5, Q9 M6, Q10 M7; Q9 and Q10 each 'a OR b' in 4 of 7 (B1 2026-27, D1, D2 2025-26, G2 2025); B1 2024-25 was 'any 10 of 12'.",
    },
    "predicted_topics": topics,
    "no_clear_pattern": [
        "Which slot-1 question reappears in slot 2: slot-pair same-archetype rate 0.69 equals the different-year baseline 0.67 (observed), so C1 does not predict C2 beyond the syllabus",
        "Verbatim reuse of older questions: 0 identical in 2026-27 papers (max text similarity 0.60)",
        "Step-mark splits: stated in only 19 of 96 answer-key rows; penalty rules in 2 of 96",
        "Knowledge representation (frames, semantic nets, expert systems): appears only in CAT1 E1 2024-25 Q2b and sister papers",
        "Which M6 sub-type (STRIPS vs hierarchical) is asked: both occur, alternated via the Q9 OR choice",
    ],
    "slot_pair_hit_rates": {
        "Identical": sp["Identical"], "Same concept new numbers": sp["Same concept new numbers"],
        "Same module only": sp["Same module only"], "Unrelated": sp["Unrelated"],
        "_n": f'{d["slot_pairs_pooled"]["n_questions"]} questions in {d["slot_pairs_pooled"]["n_pairs"]} slot pairs',
        "_baseline_different_year_same_concept": d["different_year_pooled_null"]["rate"]["Same concept new numbers"],
        "_cross_letter_same_year_same_concept": d["cross_letter_pooled"]["rate"]["Same concept new numbers"],
        "_sister_courses_same_concept": d["sister_pooled"]["rate"]["Same concept new numbers"],
    },
}
json.dump(out, open(f"{B}/patterns.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("patterns.json:", len(topics), "topics; top 10:", [t["topic_id"] for t in topics[:10]])
