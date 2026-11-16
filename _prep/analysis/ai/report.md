# AI (BCSE306L): FAT pattern report for slot C2 (Thu 19 Nov 2026)

Machine-readable version: `patterns.json`. Raw numbers: `analysis_raw.json`. Rows: `questions.csv`, `questions_text.jsonl`.
Every claim cites `file:Qn`. **O** = observed (counted directly), **I** = inferred (rule or judgement).

## 1. Data and validation

| item | value |
|---|---|
| AI files extracted | 37 (BCSE306L 27, BITE308L 5, BECE309L 4, CSI3003 1), 344 question rows |
| Distinct BCSE306L papers analysed | 25 after merging QP/AK duplicates: 7 FAT, 11 CAT-1, 7 CAT-2 (O) |
| 2026-27 BCSE306L papers | FAT B1; CAT-1 B1, B2, C1, C2; CAT-2 B2 (O) |
| Your slot's own paper | CAT-1 C2 2026-27 question paper + its official revised key (file named `...C2-2025-2026-Key.pdf`, header says Fall 2026-27 C2+TC2) (O) |
| Orchestrator re-read | 35 of 344 questions (10.2%): text 34/35, type 30/35, Bloom 30/35, scenario 33/35 (O); pooled tag agreement 0.886 |
| Marks check | 33 of 37 papers sum to stated maximum; 4 flagged, all explained in `verification.md` (O) |
| Unreadable pages | none fully unreadable; 23 rows ocr_flag=1 (O) |
| Two agents, same paper (B1 CAT-1 26-27 QP vs AK) | marks 7/7, module 7/7, Bloom 6/7, scenario 6/7, type 3/7 (O): **type is the least reliable tag** |

## 2. FAT blueprint (O, 7 FATs)

| Q | module (typical) | evidence |
|---|---|---|
| 1 | M1 agents / PEAS / environments | Q1 is M1 in 7 of 7 |
| 2-3 | M2 search (uninformed, informed, formulation) | 7 of 7 |
| 4-5 | M3 local search, minimax/alpha-beta, GA | 7 of 7 |
| 5-7 | M4 FOL, CNF, resolution, chaining | 7 of 7 |
| 7-8 | M5 Bayes, Bayesian networks, Naive Bayes | 7 of 7 |
| 9 | M6 planning, often "9a OR 9b" | OR choice in 4 of 7 |
| 10 | M7 NLP / IR / perception, often "10a OR 10b" | OR choice in 4 of 7 |

All 7 modules appear in every FAT (7 of 7). Format: 10 x 10 = 100, 3 hours. B1 2024-25 was "any 10 of 12" (O).

## 3. Ranked predictions for C2 FAT

p = (2k_recent + k_older + 1)/(2n_recent + n_older + 2). FAT-only: n_recent = 1 (B1 2026-27), n_older = 6.
"All papers" = CAT/FAT papers whose syllabus window covers the module. Small n: read as ranks.

| rank | topic | module | p (FAT) | FAT ratio | in 2026-27 FAT? | p (all) | all ratio | core type | example (fluff stripped) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | English to FOL / CNF | M4 | 0.90 | 7 of 7 | yes | 0.94 | 14 of 14 | theory | translate statements to FOL, then CNF (FAT-B1-2026-27:Q7a,b) |
| 2 | Greedy best-first / A* | M2 | 0.80 | 6 of 7 | yes | 0.88 | 16 of 18 | trace | expansion order + path for DFS, BFS, A* (FAT-B1-2026-27:Q4) |
| 3 | Resolution refutation | M4 | 0.80 | 6 of 7 | yes | 0.83 | 12 of 14 | trace | prove "Curiosity killed Tuna" by resolution (FAT-B1-2026-27:Q7c) |
| 4 | NLP / language models / IR | M7 | 0.80 | 6 of 7 | yes | 0.80 | 6 of 7 | theory | unigram/bigram/trigram models (FAT-B1-2026-27:Q8) |
| 5 | Uninformed search trace (BFS/DFS/DLS/IDS) | M2 | 0.80 | 6 of 7 | yes | 0.68 | 13 of 18 | trace | same as rank 2 (FAT-B1-2026-27:Q4) |
| 6 | Minimax + alpha-beta | M3 | 0.80 | 6 of 7 | yes | 0.52 | 14 of 25 | trace | minimax values, then alpha-beta prunes (FAT-B1-2026-27:Q6a,b) |
| 7 | STRIPS / classical planning | M6 | 0.70 | 6 of 7 | no | 0.70 | 6 of 7 | theory | STRIPS + partial-order plan, blocks world (FAT-D1-2025-26:Q9a) |
| 8 | Hierarchical (HTN) planning | M6 | 0.70 | 5 of 7 | yes | 0.70 | 5 of 7 | theory | hierarchical planning, HLAs vs primitives (FAT-B1-2026-27:Q10a) |
| 9 | Bayesian network inference | M5 | 0.70 | 5 of 7 | yes | 0.56 | 8 of 14 | numerical | joint P(A,J,M,~B,~E) alarm network (FAT-B1-2026-27:Q9a) |
| 10 | Hill climbing + simulated annealing | M3 | 0.70 | 5 of 7 | yes | 0.46 | 11 of 25 | trace | hill climbing from A, does it reach M? (FAT-B1-2026-27:Q5) |
| 11 | PEAS + environment properties | M1 | 0.60 | 5 of 7 | no | 0.84 | 16 of 18 | theory | PEAS + 6 dimensions (FAT-D1-2025-26:Q1; CAT1-C2-2026-27:Q2) |
| 12 | Formulation / 8-puzzle parity | M2 | 0.60 | 4 of 7 | yes | 0.64 | 11 of 18 | numerical | inversion parity + Manhattan solve (FAT-B1-2026-27:Q3) |
| 13 | Bayes' rule / total probability | M5 | 0.60 | 5 of 7 | no | 0.56 | 9 of 14 | numerical | P(T) by total probability, P(C2|T) (FAT-D1-2025-26:Q7b) |
| 14 | AI foundations / types | M1 | 0.60 | 5 of 7 | no | 0.40 | 8 of 18 | theory | (FAT-D1-2025-26:Q1) |
| 15 | Agent types & rationality | M1 | 0.50 | 3 of 7 | yes | 0.76 | 13 of 18 | theory | true/false on rationality (FAT-B1-2026-27:Q1, Q2) |
| 16 | Propositional inference / truth tables | M4 | 0.50 | 4 of 7 | no | 0.72 | 11 of 14 | trace | validity by rules of inference (FAT-D1-2025-26:Q5a) |
| 17 | Forward / backward chaining | M4 | 0.50 | 4 of 7 | no | 0.61 | 9 of 14 | trace | forward chaining "Curiosity killed the cat" (FAT-D1-2025-26:Q5b) |
| 18 | Uniform cost search | M2 | 0.40 | 3 of 7 | no | 0.52 | 9 of 18 | trace | UCS frontier per step (CAT1-C2-2026-27:Q3a) |
| 19 | Genetic algorithm | M3 | 0.40 | 3 of 7 | no | 0.27 | 7 of 25 | numerical | GA job scheduling (FAT-E2-2024:Q5) |
| 20 | Naive Bayes | M5 | 0.30 | 2 of 7 | no | 0.44 | 7 of 14 | numerical | classify loan applicant (FAT-D1-2025-26:Q8) |
| 21 | Object recognition / image retrieval | M7 | 0.30 | 2 of 7 | no | 0.30 | 2 of 7 | theory | (FAT-D1-2025-26:Q10b) |

Suggested teach order (I): tier p >= 0.75 by module (M2 search -> M3 minimax -> M4 FOL/CNF/resolution -> M7 NLP), then tier 0.55-0.75 (M1 PEAS/env, M2 8-puzzle, M3 local search, M5 Bayes net + Bayes rule, M6 STRIPS + HTN), then the rest. `teach_order` in patterns.json.

## 4. Drift: do 2026-27 papers break the baseline? (O; 2026-27 n is 1-4 papers per exam)

| exam | metric | older | 2026-27 |
|---|---|---|---|
| CAT-1 | mean Bloom | 3.20 (7 papers) | 3.18 (4 papers) |
| CAT-1 | scenario wrapper % of questions | 26.1 | 30.3 |
| CAT-1 | theory % of marks | 41.3 | 55.0 |
| CAT-1 | (numerical+trace) : theory marks | 0.80 | 0.60 |
| CAT-2 | scenario wrapper % of questions | 24.5 (6) | 80.0 (1 paper: B2) |
| CAT-2 | (numerical+trace) % of marks | 64.7 | 92.0 |
| FAT | mean Bloom | 3.26 (6) | 2.82 (1 paper: B1) |
| FAT | scenario wrapper % of questions | 27.3 | 5.9 |
| FAT | (numerical+trace) : theory marks | 1.51 | 0.77 |
| all | scenario wrapper % by start year | 2022: 12.5, 2023: 16.1, 2024: 28.4, 2025: 29.9, 2026: 31.7 | |

Reading: topics mostly follow the baseline. The 2026-27 FAT contained 6 of the 10 most frequent pre-2026 FAT archetypes (missing: STRIPS planning, AI foundations, PEAS/environment, Bayes' rule) and 5 lower-frequency ones (agent rationality, 8-puzzle parity, hill climbing, Bayes net, HTN planning) (O). Style is mixed: scenario wrappers rose steadily from 2022 to 2025 (O) and stayed flat in 2026-27 CAT-1. The one 2026-27 FAT is less scenario-heavy and more theory-heavy than older FATs. With n=1 that is **no clear pattern** for the FAT.

## 5. Slot pairs and sister courses (I: rule-based matching; see analysis_raw.json for every match)

| comparison | n questions | Identical | Same concept new numbers | Same module only | Unrelated |
|---|---|---|---|---|---|
| slot 1 vs slot 2, same exam and year (10 pairs) | 90 | 0 | 0.69 | 0.31 | 0 |
| different slot letter, same year (6 pairs, e.g. B1 vs C2) | 68 | 0 | 0.65 | 0.25 | 0.10 |
| **baseline: same exam, different year (158 pairs)** | 1412 | 0 | 0.67 | 0.30 | 0.03 |
| sister course vs BCSE306L, same exam and year (19 pairs) | 151 | 0 | 0.60 | 0.25 | 0.15 |
| sister course, same slot only (4 pairs) | 32 | 0 | 0.50 | 0.44 | 0.06 |

Rule: none. Slot-1 to slot-2 similarity (0.69) is no higher than the different-year baseline (0.67). C1 papers do not predict C2 beyond the shared syllabus. B1 FAT 2026-27 is as good a guide to C2 as any other FAT (O, small n). No question was copied verbatim from an older paper (max similarity 0.60) (O).

## 6. Answer keys: what earns marks (O; 96 key rows, 19 state step marks, 2 state penalties)

| topic | mandatory elements in real keys | source |
|---|---|---|
| UCS | PQ + visited per step (4), tree per step (3), path + cost of each goal (2), min-cost goal (1); goal test at dequeue | CAT-1-B2-2023-24:Q4; CAT1-C2-Key:Q3a |
| A* / greedy | table: path, length, f=g+h, expanded list; admissibility via h vs h* | CAT1-B1-2026-27-AK:Q5; CAT1-D1-2025-26-AK:Q4a,b |
| BFS/DFS/IDS | pop order per algorithm, 3 marks each (1.5 stack/queue + 1.5 traversal); IDS order for every limit | CAT-1-B1-2023-24:Q3a; CAT1-D2-AK:Q3 |
| Minimax / alpha-beta | value of every internal node + root move; pruned nodes with alpha/beta at each prune | CAT2-D1-2025-26-AK:Q1i-iii |
| Hill climbing / SA | algorithm 1.5 + failure 2; SA algorithm 1.5 + success 2; P = exp(deltaV/T) with a number; cooling schedule | CAT1-D1-AK:Q5; CAT1-C2-Key:Q5b |
| PEAS / environment | PEAS 4 + environment 3 + architecture diagram 3; or 2.5 per agent | CAT1-D1-AK:Q1; CAT-1-B1-2023-24:Q2 |
| Agent type | diagram 2 + explanation 3; name type + justify from scenario cues | CAT1-D1-AK:Q2a; CAT1-C2-Key:Q1a |
| Resolution | predicate form -> clause form -> negated goal -> unifiers -> empty clause | CAT-2-B1-2023-AK:Q2; CAT-2-B2-2023-AK:Q5a |
| Chaining | rules fired in order, new facts numbered A6, A7...; note rules that do not fire | CAT-2-B2-2023-AK:Q3a; CAT-2-E1-2024-AK:Q3 |
| Bayes net / Naive Bayes | factorise joint into CPT product; priors x conditionals per class, compare | CAT2-D1-AK:Q5; CAT-2-B1-2023-AK:Q5 |

Penalty rules seen: "partial marks for other agent types with justification" (CAT-1-B1-2023-24:Q1b); "students can use any problem" (CAT-1-E2-2024-25:Q5); A* partial credit for following the flow (CAT1-D2-AK:Q4) (O).

## 7. Observed traps (each from a real question or key)

Ties broken alphabetically, graph search expands a state once (FAT-B1-2026-27:Q4) · a node printed with no h value (FAT-B1-2026-27:Q4) · UCS goal test at dequeue, two optimal paths at cost 7 (CAT1-C2-Key:Q3a) · root may be MIN (CAT-2-E2-2024:Q1) · pruning order reversed in a sub-part (CAT2-D1-AK:Q1iii) · "does hill climbing reach M?" (FAT-B1-2026-27:Q5c) · 8-puzzle inversion count ignores the blank (FAT-B1-2026-27:Q3) · "exactly one" needs uniqueness (CAT-2-E2-2024:Q3A) · ~B, ~E in a joint need 1-P (FAT-B1-2026-27:Q9a) · zero count kills a Naive Bayes class (CAT-2-E1-2024-AK:Q5) · fleet of drones = multi-agent (CAT1-C2-2026-27:Q2b) · route scoring = utility-based (CAT1-C2-Key:Q1a).

## 8. No clear pattern

Slot-specific reuse · verbatim reuse · step-mark splits (19/96) · knowledge representation (frames, semantic nets) · which M6 sub-type is asked (both, via OR) · FAT style drift (n=1).
