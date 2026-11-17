# FAT pattern analysis: summary (Fall 2026-27)

Per-subject detail: `<subject>/report.md` and `<subject>/patterns.json`. All rows: `questions.csv` (pipe-delimited). O = observed count, I = inferred. Probability = (2k_recent + k_older + 1)/(2n_recent + n_older + 2) over the course's FATs. Read as ranks, not chances.

## Corpus and validation

| subject | slot | rows | papers flagged on marks | rows ocr_flag=1 | orchestrator re-read: rows, pooled tag agreement | FATs used (2026-27) |
|---|---|---|---|---|---|---|
| AI BCSE306L | C2 | 344 | 2 | 23 | 35, 0.886 | 7 (1) |
| DBS BCSE302L | D2 | 585 | 12 | 34 | 15, 0.8 | 11 (0) |
| CN BCSE308L | F2 | 618 | 8 | 53 | 13, 0.846 | 11 (0) |
| CD BCSE307L | G2 | 234 | 5 | 57 | 14, 0.595 | 7 (0) |
| OS BCSE303L | done | 337 | 6 | 37 | not re-read (backtest only) | 11 (4) |
| AWS BCSE355L | done | 181 | 1 | 6 | not re-read (backtest only) | 9 (4) |

Inventory: 254 PDFs, 217 unique by hash; 24 files end in -AK.pdf; 48 answer keys by name (40 unique). Backtest (OS+AWS, 4 slot-2 FATs): 22 of 40 top-10 topics hit, tier Medium; plain frequency also 22 of 40.

## AI (BCSE306L Artificial Intelligence): slot C2

| rank | topic | module | p | FAT ratio | 2026-27 evidence | core type |
|---|---|---|---|---|---|---|
| 1 | English to FOL / CNF conversion | M4 | 0.90 | 7 of 7 | 1 of 1 FATs 2026-27 | theory |
| 2 | Informed search: Greedy best-first / A* / heuristics | M2 | 0.80 | 6 of 7 | 1 of 1 FATs 2026-27 | trace |
| 3 | Resolution refutation proof (prop./FOL) | M4 | 0.80 | 6 of 7 | 1 of 1 FATs 2026-27 | trace |
| 4 | NLP, language models, information retrieval/extraction | M7 | 0.80 | 6 of 7 | 1 of 1 FATs 2026-27 | theory |
| 5 | Uninformed search trace (BFS/DFS/DLS/IDS) | M2 | 0.80 | 6 of 7 | 1 of 1 FATs 2026-27 | trace |
| 6 | Minimax + alpha-beta pruning | M3 | 0.80 | 6 of 7 | 1 of 1 FATs 2026-27 | trace |
| 7 | STRIPS / classical planning (blocks world, POP, planning graph) | M6 | 0.70 | 6 of 7 | 0 of 1 FATs 2026-27 | theory |
| 8 | Hierarchical (HTN) planning, multi-agent planning | M6 | 0.70 | 5 of 7 | 1 of 1 FATs 2026-27 | theory |
| 9 | Bayesian network inference (joint / conditional from CPTs) | M5 | 0.70 | 5 of 7 | 1 of 1 FATs 2026-27 | numerical |
| 10 | Hill climbing + simulated annealing | M3 | 0.70 | 5 of 7 | 1 of 1 FATs 2026-27 | theory |
| 11 | PEAS + task-environment properties | M1 | 0.60 | 5 of 7 | 0 of 1 FATs 2026-27 | theory |
| 12 | Problem formulation / state space (8-puzzle heuristics & parity, river crossing, water jug, Hanoi) | M2 | 0.60 | 4 of 7 | 1 of 1 FATs 2026-27 | trace |

| finding | value |
|---|---|
| slot 1 -> slot 2 same archetype | 0.69 (90 questions in 10 slot pairs) vs different-year baseline 0.67 (O) |
| identical questions slot 1 -> slot 2 | 0.00 (O) |
| backtest confidence | Medium (22 of 40) |
| tag agreement (orchestrator re-read) | 0.886 |
| no clear pattern | Which slot-1 question reappears in slot 2: slot-pair same-archetype rate 0.69 equals the different-year baseline 0.67 (observed), so C1 does not predict C2 beyond the syllabus; Verbatim reuse of older questions: 0 identical in 2026-27 papers (max text similarity 0.60); Step-mark splits: stated in only 19 of 96 answer-key rows; penalty rules in 2 of 96 |

## DBS (BCSE302L Database Systems): slot D2

| rank | topic | module | p | FAT ratio | 2026-27 evidence | core type |
|---|---|---|---|---|---|---|
| 1 | DBMS architecture / data independence | M1 | 0.92 | 11 of 11 | CATs 2 of 2; sister FATs 3 of 3 | theory |
| 2 | 2PL / locking | M6 | 0.85 | 10 of 11 | CATs 0 of 2; sister FATs 2 of 3 | trace |
| 3 | Indexing / B+ tree | M4 | 0.85 | 10 of 11 | CATs 0 of 2; sister FATs 2 of 3 | trace |
| 4 | Normalization (1NF-BCNF) | M3 | 0.85 | 10 of 11 | CATs 2 of 2; sister FATs 3 of 3 | numerical |
| 5 | NoSQL types / CAP | M7 | 0.77 | 9 of 11 | CATs 0 of 2; sister FATs 3 of 3 | theory |
| 6 | Schedules / conflict serializability | M6 | 0.69 | 8 of 11 | CATs 0 of 2; sister FATs 3 of 3 | trace |
| 7 | ER diagram design | M2 | 0.61 | 7 of 11 | CATs 1 of 2; sister FATs 1 of 3 | scenario |
| 8 | ER to relational mapping | M2 | 0.54 | 6 of 11 | CATs 1 of 2; sister FATs 0 of 3 | theory |
| 9 | Relational algebra | M2 | 0.54 | 6 of 11 | CATs 0 of 2; sister FATs 1 of 3 | theory |
| 10 | Deadlock (wait-die / wound-wait) | M6 | 0.46 | 5 of 11 | CATs 0 of 2; sister FATs 1 of 3 | theory |
| 11 | Transactions ACID / states | M5 | 0.46 | 5 of 11 | CATs 0 of 2; sister FATs 1 of 3 | theory |
| 12 | Hashing | M4 | 0.46 | 5 of 11 | CATs 0 of 2; sister FATs 1 of 3 | numerical |

| finding | value |
|---|---|
| slot 1 -> slot 2 same archetype | 0.66 (90 questions in 10 slot pairs) vs different-year baseline 0.57 (O) |
| identical questions slot 1 -> slot 2 | 0.00 (O) |
| backtest confidence | Medium (22 of 40) |
| tag agreement (orchestrator re-read) | 0.8 |
| no clear pattern | Slot-pair reuse: slot 1 -> slot 2 same-archetype rate 0.66 vs different-year baseline 0.57 (small lift, 90 questions); 2026-27 FAT style (no 2026-27 BCSE302L FAT in corpus); SQL query writing in FATs: 2 of 11 |

## CN (BCSE308L Computer Networks): slot F2

| rank | topic | module | p | FAT ratio | 2026-27 evidence | core type |
|---|---|---|---|---|---|---|
| 1 | IPv4 addressing / subnetting / CIDR | M4 | 0.92 | 11 of 11 | CATs 2 of 4; sister FATs 2 of 2 | numerical |
| 2 | Circuit vs packet switching | M2 | 0.77 | 9 of 11 | CATs 2 of 4; sister FATs 1 of 2 | theory |
| 3 | MAC (ALOHA/CSMA/CD/CA) | M3 | 0.77 | 9 of 11 | CATs 1 of 4; sister FATs 2 of 2 | numerical |
| 4 | Topologies / network types | M1 | 0.69 | 8 of 11 | CATs 1 of 4; sister FATs 0 of 2 | scenario |
| 5 | Distance vector routing | M5 | 0.69 | 8 of 11 | CATs 1 of 4; sister FATs 1 of 2 | theory |
| 6 | TCP congestion control | M6 | 0.69 | 8 of 11 | CATs 0 of 4; sister FATs 1 of 2 | theory |
| 7 | Link state / Dijkstra | M5 | 0.69 | 8 of 11 | CATs 1 of 4; sister FATs 0 of 2 | trace |
| 8 | Error detection (CRC/checksum/parity) | M3 | 0.69 | 8 of 11 | CATs 2 of 4; sister FATs 2 of 2 | numerical |
| 9 | Delay / throughput calculation | M2 | 0.61 | 7 of 11 | CATs 2 of 4; sister FATs 1 of 2 | numerical |
| 10 | IP fragmentation | M4 | 0.61 | 7 of 11 | CATs 2 of 4; sister FATs 1 of 2 | numerical |
| 11 | OSI vs TCP/IP layers | M1 | 0.54 | 6 of 11 | CATs 2 of 4; sister FATs 1 of 2 | theory |
| 12 | DNS | M7 | 0.46 | 5 of 11 | CATs 0 of 4; sister FATs 0 of 2 | theory |

| finding | value |
|---|---|
| slot 1 -> slot 2 same archetype | 0.73 (132 questions in 9 slot pairs) vs different-year baseline 0.65 (O) |
| identical questions slot 1 -> slot 2 | 0.00 (O) |
| backtest confidence | Medium (22 of 40) |
| tag agreement (orchestrator re-read) | 0.846 |
| no clear pattern | Exact question numbering of modules (F1/F2 2025-26 placed M3 last); Application-layer protocol choice: DNS 5/11, HTTP 4/11, SMTP 3/11, FTP 3/11; Step-mark splits: rarely stated |

## CD (BCSE307L Compiler Design): slot G2

| rank | topic | module | p | FAT ratio | 2026-27 evidence | core type |
|---|---|---|---|---|---|---|
| 1 | SDD / SDT / annotated parse tree | M3 | 0.89 | 7 of 7 | CATs 0 of 3; sister FATs 0 of 0 | trace |
| 2 | Phases of compiler | M1 | 0.78 | 6 of 7 | CATs 2 of 3; sister FATs 0 of 0 | trace |
| 3 | Three-address code / quadruples / triples | M4 | 0.78 | 6 of 7 | CATs 1 of 3; sister FATs 0 of 0 | trace |
| 4 | Code generation / register allocation | M6 | 0.78 | 6 of 7 | CATs 0 of 3; sister FATs 0 of 0 | theory |
| 5 | Code optimization (CSE/constant folding/loop) | M5 | 0.78 | 6 of 7 | CATs 0 of 3; sister FATs 0 of 0 | theory |
| 6 | Basic blocks / flow graph | M4 | 0.78 | 6 of 7 | CATs 1 of 3; sister FATs 0 of 0 | trace |
| 7 | Instruction scheduling / ILP | M7 | 0.67 | 5 of 7 | CATs 0 of 3; sister FATs 0 of 0 | theory |
| 8 | Backpatching | M4 | 0.67 | 5 of 7 | CATs 0 of 3; sister FATs 0 of 0 | trace |
| 9 | CLR / LALR parsing | M2 | 0.67 | 5 of 7 | CATs 1 of 3; sister FATs 0 of 0 | trace |
| 10 | Direct RE to DFA | M1 | 0.56 | 4 of 7 | CATs 2 of 3; sister FATs 0 of 0 | trace |
| 11 | Syntax tree / DAG | M4 | 0.56 | 4 of 7 | CATs 1 of 3; sister FATs 0 of 0 | trace |
| 12 | LL(1) parsing table | M2 | 0.56 | 4 of 7 | CATs 1 of 3; sister FATs 0 of 0 | trace |

| finding | value |
|---|---|
| slot 1 -> slot 2 same archetype | 0.51 (70 questions in 8 slot pairs) vs different-year baseline 0.58 (O) |
| identical questions slot 1 -> slot 2 | 0.00 (O) |
| backtest confidence | Medium (22 of 40) |
| tag agreement (orchestrator re-read) | 0.595 |
| no clear pattern | Slot-pair reuse: slot 1 -> slot 2 same-archetype 0.51 vs different-year baseline 0.58 (70 questions): slot pairing gives no lift; Scenario-wrapper drift: tags unreliable for CD (2/14 agreement); Exact FAT question order (shuffled in 2 of 7) |

## Flags

| item | value |
|---|---|
| fully unreadable files | none; every page was read from images (PyMuPDF renders, verified wheel) |
| misfiled | `CN/PYQ/FAT/BCSE308L - FAT - B1 - 2024 - Question Paper (2).pdf` = BECE308L Optical Fiber Communications (excluded) |
| wrong year in filename | `AI/PYQ/CAT1/BCSE306L-CAT1-C2-2025-2026-Key.pdf` = Fall 2026-27 CAT-I C2 revised key (your slot) |
| same-label different papers (kept separate) | DBS FAT-A2-2024 vs FAT-A2-2024-2025; CAT-2-B2-Winter-2025-26 vs CAT2-B2-2025-26-AK; CAT-1-B2-2025-26 vs its AK-named file; FAT-A1-2024-25 vs Model FAT (Model FAT excluded) |
| whole papers shared across slots (merged) | CN CAT-1 B1 = D1 (2023-24); CN CAT-2 D1 = F1 (2023-24) |
| answer keys with arithmetic errors (transcribed as printed) | CN CAT-2 D2 2024-25 (0.18 x 56 Kbps printed 10.3); CN CAT-2 F2 2025-26 Q5; CN CAT-2 D1 2023-24 Q2 |
| re-dispatched shards (once each) | AI-D1, AI-D2, AI-D3 (figures lost: no PDF rasteriser), AI-D4 figure fill, CN-D1 (condensed text) |
| re-read below 10% | DBS 2.6%, CN 2.1%, CD 6.0% (AI 10.2%); OS/AWS used only for backtest |

## Authorship note (hypothesis, not a finding)

The brief asked not to assume LLM use, so only style metrics were measured (O = counted on BCSE core papers; one row per question; 2026-27 samples are 2-6 papers per subject).

| metric by start year | AI | OS | AWS | DBS | CN | CD |
|---|---|---|---|---|---|---|
| scenario-wrapped questions, 2026 vs highest earlier year | 34% vs 30% | 60% vs 44% | 84% vs 65% | 53% vs 38% | 71% vs 39% | 68% vs 19% (tag unreliable) |
| mean words per question, 2026 vs highest earlier year | 51 vs 59 | 53 vs 55 | 64 vs 65 | 58 vs 61 | 74 vs 61 | 86 vs 59 |
| mean Bloom, 2026-27 vs older (CAT-1) | 3.18 vs 3.20 | n/a | n/a | 2.73 vs 3.50 | 3.14 vs 3.16 | 3.10 vs 3.36 |

Evidence for a change in how questions are drafted: across all CAT and FAT rows, scenario framing is at its highest in 2026-27 in all six subjects (CD's tag is unreliable). CN and CD 2026-27 questions are much longer. Several 2026-27 prompts carry explicit assumption lists and negative constraints, for example "Do not present separate final conditions" (BCSE307L-CAT2-G2-2026-2027:Q2b) and "Do not construct a CFG or apply optimization" (BCSE307L-CAT2-G2-2026-2027:Q5b).

Evidence against: topics and archetypes are unchanged (no subject breaks its baseline). Bloom level is flat or lower. The one 2026-27 AI FAT is less scenario-framed than older AI FATs. AI and DBS questions are not longer. Scenario framing was rising before 2026-27 (AI 12% in 2022 to 30% in 2025; OS 18% in 2024 to 44% in 2025; AWS already 63% in 2024). Wrapper tags are noisy (verified agreement 2/14 for CD, 9/13 for CN, 13/15 for DBS). A department-level template change (papers "Common to all", set by 20+ faculty) explains the same pattern.

Hypothesis: 2026-27 papers show a measurable shift toward longer, scenario-framed, constraint-heavy prompts in CN and CD, and partly in OS, AWS and DBS. The data cannot separate LLM-assisted drafting from a template or moderation change. Treat as unproven. It does not change what to study.
