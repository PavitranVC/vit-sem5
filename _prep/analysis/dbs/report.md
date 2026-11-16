# DBS (BCSE302L Database Systems): FAT pattern report for slot D2

Machine-readable: `patterns.json`. Raw numbers: `analysis_raw.json`. Rows: `questions.csv`, `questions_text.jsonl`.
**O** = observed (counted), **I** = inferred (rule or judgement). Every claim cites file:Qn.

## 1. Data and validation

| item | value |
|---|---|
| question rows (all codes) | 585 |
| distinct BCSE302L papers (QP/AK duplicates merged by text similarity >= 0.6) | 30: 11 FAT (0 from 2026-27), 10 CAT-1, 9 CAT-2 (O) |
| 2026-27 sister-course FATs | 3: BACSE202-FAT-A1-2026-2027, BACSE202-FAT-A2-2026-2027, CBS1007-FAT-A2-2026-2027 (O) |
| orchestrator re-read | 15 questions re-read (BCSE302L-CAT1-D2-2026-2027 Q1a-Q5b, BCSE302L-CAT1-D1-2026-2027 Q1a-Q5b): text 15/15, type 11/15, bloom 12/15, scenario 13/15; pooled 36/45 = 0.80. Below the 10% target (585 rows) because of context limits; disagreements follow the AI pattern (agents tag explain/identify tasks with a narrative opener as 'scenario'). (O) |
| marks check | 12 papers flagged (unprinted per-question marks, OR alternatives, case-study items); see validation.md (O) |
| rows with ocr_flag=1 | 34 (O) |
| backtest confidence (OS+AWS) | Medium: 22 of 40; naive frequency list 22 of 40 (O) |

## 2. FAT blueprint (O)

10 x 10 FAT in 9 of 11; all 7 modules in 10 of 11 FATs. Typical order Q1 M1 (architecture / data independence, 11 of 11), Q2-Q3 M2 (ER/EER, mapping, relational algebra), Q3-Q4 M3 (normalization), Q5-Q6 M4 (indexing / B+ tree, query optimisation), Q7-Q8 M5-M6 (transactions, serializability, 2PL), Q9-Q10 M6-M7 (concurrency, NoSQL/CAP), with 'Q9 a or b; Q10 a or b' in 3 of 11. No 2026-27 BCSE302L FAT exists in the corpus; 2026-27 evidence is CAT-1 D1 and D2 (your slot letter) plus 3 sister FATs (BACSE202 A1/A2, CBS1007 A2).

## 3. Ranked topics for slot D2

p = (2k_recent + k_older + 1)/(2n_recent + n_older + 2) over BCSE302L FATs (n_recent=0, n_older=11). 'all' = CAT/FAT papers covering the module.

| rank | topic | mod | p (FAT) | FAT ratio | p (all) | all ratio | 2026-27 CATs (of 2) | 2026-27 sister FATs (of 3) | core type | example (fluff stripped) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DBMS architecture / data independence | M1 | 0.92 | 11 of 11 | 0.96 | 21 of 21 | 2 | 3 | theory | Identify suitable data model for multi-branch retail system; explain characteristics, benefits, user categories, DBA responsibilities (cite BCSE302L-C |
| 2 | 2PL / locking | M6 | 0.85 | 10 of 11 | 0.85 | 10 of 11 | 0 | 2 | trace | Draw a 2PL schedule for T1, T2, T3, show where deadlock can occur and how to avoid or resolve it. (cite BCSE302L-FAT-B2-2025-2026:Q9a) |
| 3 | Indexing / B+ tree | M4 | 0.85 | 10 of 11 | 0.82 | 17 of 20 | 0 | 2 | trace | Explain multilevel indexing techniques with real-world examples. (cite BCSE302L-FAT-B2-2025-2026:Q5) |
| 4 | Normalization (1NF-BCNF) | M3 | 0.85 | 10 of 11 | 0.77 | 23 of 30 | 2 | 3 | numerical | Check 2NF of ENROLLMENT, decompose to 2NF then 3NF, show relations with primary keys (cite BCSE302L-CAT1-D1-2026-2027:Q5b) |
| 5 | NoSQL types / CAP | M7 | 0.77 | 9 of 11 | 0.77 | 9 of 11 | 0 | 3 | theory | Explain the CAP theorem for NoSQL databases and its influence on distributed design trade-offs. (cite BCSE302L-FAT-B2-2025-2026:Q10a) |
| 6 | Schedules / conflict serializability | M6 | 0.69 | 8 of 11 | 0.69 | 8 of 11 | 0 | 3 | trace | Test conflict-serializability of S1, S2, S3, draw precedence graphs, build a serializable T1/T2 schedule and explain. (cite BCSE302L-FAT-B2-2025-2026: |
| 7 | ER diagram design | M2 | 0.61 | 7 of 11 | 0.41 | 12 of 30 | 1 | 1 | scenario | Draw ER diagram with entities, attributes, keys, relationships, cardinality, participation for university (cite BCSE302L-CAT1-D2-2026-2027:Q3) |
| 8 | ER to relational mapping | M2 | 0.54 | 6 of 11 | 0.50 | 15 of 30 | 1 | 0 | theory | Convert given customer-borrower-loan ER diagram into relational tables with primary and foreign keys (cite BCSE302L-CAT1-D2-2026-2027:Q4b) |
| 9 | Relational algebra | M2 | 0.54 | 6 of 11 | 0.44 | 14 of 30 | 0 | 1 | theory | Express five library queries (borrowers of Database Systems, Pearson titles, unreturned borrowers, publisher counts, never-borrowed titles) in relatio |
| 10 | Deadlock (wait-die / wound-wait) | M6 | 0.46 | 5 of 11 | 0.46 | 5 of 11 | 0 | 1 | theory | Analyze common causes of deadlocks in lock-based concurrency control (cite BCSE302L-FAT-B1-2025-2026:Q10bi) |
| 11 | Transactions ACID / states | M5 | 0.46 | 5 of 11 | 0.46 | 5 of 11 | 0 | 1 | theory | Illustrate the various states of a database transaction. (cite BCSE302L-FAT-B2-2025-2026:Q8a) |
| 12 | Hashing | M4 | 0.46 | 5 of 11 | 0.41 | 8 of 20 | 0 | 1 | numerical | Insert Account_No keys into 7-bucket hash file (h(K)=K mod 7, two records per bucket); show buckets and overflow. (cite BCSE302L-FAT-E1-2025-2026:Q6a) |
| 13 | Query processing / optimization | M4 | 0.39 | 4 of 11 | 0.55 | 11 of 20 | 0 | 3 | trace | Build initial and heuristically optimized query trees for the EMP/PROJ/ASG query. (cite BCSE302L-CAT2-B1-2025-2026-AK:Q4) |
| 14 | Timestamp ordering | M6 | 0.39 | 4 of 11 | 0.39 | 4 of 11 | 0 | 0 | trace | Trace BTO read/write timestamps for schedule, note rejections, and test conflict serializability with serial order. (cite BCSE302L-FAT-E1-2025-2026:Q9 |
| 15 | Log-based recovery / checkpoints | M5 | 0.39 | 4 of 11 | 0.39 | 4 of 11 | 0 | 1 | trace | List log entries for the timeline under NO-UNDO/REDO and UNDO/REDO; state redo/undo needs after crash. (cite BCSE302L-FAT-E1-2025-2026:Q7bi) |
| 16 | ARIES / shadow paging | M5 | 0.39 | 4 of 11 | 0.39 | 4 of 11 | 0 | 0 | theory | Discuss the shadow paging technique, its working and significance in detail. (cite BCSE302L-FAT-B2-2025-2026:Q8b) |
| 17 | EER / specialization | M2 | 0.39 | 4 of 11 | 0.38 | 10 of 30 | 2 | 2 | theory | Design EER diagram with specialization for bank customer hierarchy with constraints (cite BCSE302L-CAT1-D1-2026-2027:Q4) |
| 18 | Functional dependencies / closure | M3 | 0.39 | 4 of 11 | 0.35 | 10 of 30 | 1 | 0 | numerical | Derive AD->E from F using inference rules (cite BCSE302L-CAT1-D1-2026-2027:Q5a) |
| 19 | Recoverable / cascadeless schedules | M5 | 0.31 | 3 of 11 | 0.31 | 3 of 11 | 0 | 1 | theory | Determine whether schedule S2 is strict, cascadeless, recoverable or nonrecoverable, with justification. (cite BCSE302L-CAT2-E1-2025-2026:Q5b) |
| 20 | Lossless / dependency-preserving decomposition | M3 | 0.31 | 3 of 11 | 0.18 | 5 of 30 | 0 | 1 | theory | Explain why nulls should be avoided and how spurious tuples are prevented. (cite BCSE302L-CAT1-B1-2025-2026-AK:Q4b) |
| 21 | SQL queries | M2 | 0.23 | 2 of 11 | 0.21 | 6 of 30 | 0 | 1 | theory | Write SQL to list names and countries of players who played on 2024-05-10. (cite BCSE302L-CAT1-E1-2025-2026:Q3a) |
| 22 | Minimal cover | M3 | 0.23 | 2 of 11 | 0.15 | 4 of 30 | 0 | 0 | numerical | Derive FDs from stated assumptions and compute the minimal cover step by step. (cite BCSE302L-FAT-E1-2025-2026:Q3a) |

Teach order (I): tier p >= 0.75 by module, then 0.50-0.75, then the rest (`teach_order`).

## 4. Drift: 2026-27 vs older (O; small n)

| exam | group | papers | mean Bloom | scenario wrapper % q | theory % marks | (num+trace):theory |
|---|---|---|---|---|---|---|
| CAT1 | older | 8 | 3.5 | 29.7 | 61.9 | 0.21 |
| CAT1 | recent_2026_27 | 2 | 2.73 | 53.3 | 10.0 | 2.5 |
| CAT2 | older | 9 | 3.03 | 35.6 | 31.1 | 2.04 |
| FAT | older | 11 | 3.19 | 24.6 | 53.0 | 0.64 |
| all | scenario wrapper % by start year | 2022: 33.3, 2023: 28.6, 2024: 13.3, 2025: 38.1, 2026: 53.3 | | | | |

2026-27 CAT-1 (D1, D2): scenario-wrapped questions 53% vs 30% in older CAT-1s, mean Bloom 2.73 vs 3.50 (O, 2 papers). By start year the scenario share went 33, 29, 13, 38, 53%: rising since 2024 but not monotonic. Caveat (O from verification): the 2026-27 CAT-1 'theory % marks' of 10 is depressed because extractors tagged explain/identify questions with a narrative opener as type 'scenario' (4 of 15 verified rows); read the scenario-wrapper % instead.

## 5. Slot pairs and sister courses (I: rule-based matching)

| comparison | n q | Identical | Same concept new numbers | Same module only | Unrelated |
|---|---|---|---|---|---|
| slot 1 -> slot 2, same exam+year (10 pairs) | 90 | 0.0 | 0.656 | 0.344 | 0.0 |
| different letter, same year (17 pairs) | 240 | 0.0 | 0.446 | 0.475 | 0.079 |
| baseline: same exam, different year (212 pairs) | 2453 | 0.01 | 0.575 | 0.382 | 0.033 |
| sister course vs core, same exam+year (26 pairs) | 306 | 0.0 | 0.454 | 0.448 | 0.098 |

Slot 1 -> slot 2 shares the archetype for 0.66 of questions vs 0.58 between different years (O). A small lift; D1 2026-27 CAT-1 is a reasonable guide to D2-style questions but does not determine them. No verbatim reuse in 2026-27 (max similarity 0.66: CAT1-D2-2026-2027:Q5a vs CAT1-E1-2025-2026:Q5ai).

## 6. Answer keys: what earns marks (O)

44 key rows; step marks stated in 16; penalties stated in 0.

| topic | mandatory elements from real keys |
|---|---|
| DBMS architecture / data independence | key shows: logical: change conceptual schema without changing external schemas or programs; physical: change internal schema without changing conceptual schema [BCSE302L-CAT1-B1-2025-2026-AK:Q1b]<br>marks: Situation a: 5 marks (three-tier justification and diagram); key shows: three-tier; client; application server; database system; business logic separated from database [BCSE302L-CAT1-B2-2025-2026-AK:Q1a] |
| Indexing / B+ tree | key shows: tree after inserting 27 and 1: root 0015; internal 0003 0006 0010 and 0020 0027; leaves 0001 through 0030 linked in order [BCSE302L-CAT2-B2-2025-2026-AK:Q3a]<br>key shows: deletion of 20, 8, 15; root 0017; internal 0003 0006 0010 and 0025 0027; leaves 0001 to 0030 with 0017, 0025, 0027, 0030 [BCSE302L-CAT2-B2-2025-2026-AK:Q3b] |
| Normalization (1NF-BCNF) | key shows: ABD+ = all attributes; candidate key ABD; 3NF violated by AB->C, AD->GH, BD->EF, A->I, H->J; R1(AB,C) R2(AD,GH) R3(BD,EF) R4(A,I) R5(H,J) R6(ABD) [BCSE302L-CAT1-B1-2025-2026-AK:Q5a]<br>key shows: insertion anomaly; deletion anomaly; update anomaly; examples [BCSE302L-CAT1-B1-2025-2026-AK:Q5b] |
| Schedules / conflict serializability | key shows: A = 230; B = 415.2; conflicts W-R (t4,t5), W-R (t10,t12), W-W (t10,t14); isolation at risk; dirty read; lost update discussed [BCSE302L-CAT2-B1-2025-2026-AK:Q5]<br>key shows: S1 conflicts T2->T3, T2->T1, T3->T1, T3->T4, T1->T4, T2->T4; S1 precedence graph acyclic; equivalent serial T2 T3 T1 T4; S2 conflicts give cycle (T1->T4->T3->T1 [BCSE302L-CAT2-B2-2025-2026-AK:Q5] |
| ER diagram design | key shows: COURSE (PK Course_ID); COURSE_OFFERING (PK Offering_ID, FK Course_ID); STUDENT (PK Student_ID); INSTRUCTOR (PK Instructor_ID); PROCTOR subtype of INSTRUCTOR; en [BCSE302L-CAT1-B1-2025-2026-AK:Q2]<br>marks: 5 marks ER diagram; key shows: Exam (exam_id, time); Course (c-number, name, department); Section weak entity (partial key s-number, enrollment) identifying Course; Room (r-number, capacity,  [BCSE302L-CAT1-B2-2025-2026-AK:Q3a] |
| ER to relational mapping | key shows: PKs: P_ID, D_ID, N_ID, R_ID, Room_ID, Bill_ID, Report_ID, Record_No; FKs: P_ID in BILL and TEST_REPORT, D_ID in CONSULTS, Room_ID in ASSIGNED; CONSULTS M:N; ASS [BCSE302L-CAT1-B1-2025-2026-AK:Q3]<br>marks: Part A 8 marks: strong, weak and relationship sets; key shows: student(sid,name,program); instructor(iid,name,dept,title); course(courseno,title,credits,syllabus); course_offerings(courseno,time,secno,room,year,semester); i [BCSE302L-CAT1-B2-2025-2026-AK:Q4a] |
| Relational algebra | key shows: (i) pi_AName(sigma_StName='Smith'(has_written join (borrows join Students))); (ii) pi_Title(Books join pi_BId(sigma_Keyword='database'(describes)) intersect pi_ [BCSE302L-CAT2-B1-2025-2026-AK:Q3]<br>key shows: a) pi make,model(sigma Year>=2020(Vehicles)); b) G AVG(daily_rate)(Vehicles); c) pi name,email(Renters join pi renter_id(Rentals join sigma make='Toyota'(Vehicl [BCSE302L-CAT2-B2-2025-2026-AK:Q2] |
| Query processing / optimization | key shows: initial tree: pi ENAME over sigma over EMP x PROJ x ASG; push selections down to EMP, PROJ, ASG; join on PNO then ENO; project early; key query text differs fro [BCSE302L-CAT2-B1-2025-2026-AK:Q4]<br>key shows: selection sigma name='Tom Hanks' pushed to Actors; sigma year<2010 pushed to Movies; join Casts with Actors on actor_id and Movies on movie_id; project title an [BCSE302L-CAT2-B2-2025-2026-AK:Q4] |
| EER / specialization | key shows: superclass/supertype; subclass/subtype; class/subclass relationship; EMPLOYEE with SECRETARY/TECHNICIAN; subclass member is the same real-world entity in a spec [BCSE302L-CAT1-B1-2025-2026-AK:Q4a] |
| Functional dependencies / closure | key shows: A+, D+, (AB)+ computed for F1 and F2; F1 covers F2; F2 covers F1; equivalent [BCSE302L-CAT2-B2-2025-2026-AK:Q1b] |
| Lossless / dependency-preserving decomposition | key shows: nulls waste space; unclear meaning of attributes; join problems; aggregate COUNT/SUM ambiguity; spurious tuples; join on PK/FK equality [BCSE302L-CAT1-B1-2025-2026-AK:Q4b]<br>marks: 2 dependency preservation; key shows: AB -> C not preserved; check requires join; 3NF decomposition (BD)(ABC) preferred [BCSE302L-CAT-2-A2-Fall-2024-2025-Answer Key:Q1c] |
| Candidate keys | marks: 2 candidate key; key shows: attribute closure; AB+ = ABCD; BC+ = ABCD; candidate keys AB and BC [BCSE302L-CAT-2-A2-Fall-2024-2025-Answer Key:Q1a] |
| DBMS vs file processing | key shows: Controlling Redundancy; Restricting Unauthorized Access; Persistent Storage for Program Objects; Storage Structures and Search Techniques; Backup and Recovery;  [BCSE302L-CAT1-B1-2025-2026-AK:Q1a]<br>marks: self-describing nature 2.5; insulation between programs and data with data abstraction 2.5; multiple views of data 2.5; ; key shows: self-describing (catalog); data independence / abstraction; multiple views; sharing; multiuser transaction processing [BCSE302L-CAT1-B2-2025-2026-AK:Q2] |
| File organization | key shows: records per block = 1000/100 = 10; total blocks = 10,000; splits = 2000/10 = 200; index entry 14 bytes, 71 entries per block, 141 index blocks; B+ tree suggeste [BCSE302L-CAT2-B1-2025-2026-AK:Q2] |
| 4NF / MVD | key shows: Name ->> Areacode, Phone; Name ->> likes, manufacturer [BCSE302L-CAT-2-A1-Fall-2024-2025-Answer Key:Q1b] |
| Aggregation in ER/EER | marks: EER diagram + justification 5 marks; key shows: Patient; Doctor; Medical machine; Diagnosis relationship aggregated as entity; Filling relationship; Patient History [BCSE302L-CAT1-B2-2025-2026-AK:Q3b] |

## 7. Observed traps

- Indexing / B+ tree: Insertion and deletion asked in the same question; key draws the tree after each phase [BCSE302L-CAT2-B2-2025-2026-AK:Q3b]
- Normalization (1NF-BCNF): 1NF step first moves the multivalued attribute (phone numbers) to its own table before 2NF/3NF; key splits marks 1NF 3, 2NF 3, 3NF 4 [BCSE302L-CAT1-B2-2025-2026-AK:Q5]
- Normalization (1NF-BCNF): 2NF question requires naming the candidate key AND each partial dependency [BCSE302L-CAT1-D2-2026-2027:Q5b]
- Schedules / conflict serializability: Besides the precedence graph, the key also computes final data values (A = 230, B = 415.2) and names the anomaly (dirty read / lost update) [BCSE302L-CAT2-B1-2025-2026-AK:Q5]
- ER diagram design: Business rules encode participation ('at least one', 'may or may not'); show total vs partial participation [BCSE302L-CAT1-D2-2026-2027:Q3]
- Query processing / optimization: Push selections (and projections) below joins before drawing the optimised tree [BCSE302L-CAT2-B1-2025-2026-AK:Q4]
- EER / specialization: Must state total/partial and disjoint/overlapping constraints explicitly [BCSE302L-CAT1-D1-2026-2027:Q4]

## 8. No clear pattern

- Slot-pair reuse: slot 1 -> slot 2 same-archetype rate 0.66 vs different-year baseline 0.58 (small lift, 90 questions)
- 2026-27 FAT style (no 2026-27 BCSE302L FAT in corpus)
- SQL query writing in FATs: 2 of 11
- FoodRush MongoDB case study: its 11 queries are an assignment, MongoDB aggregation appears in 1 of 11 FATs and in sister 2026-27 FATs
- Step-mark splits are rarely stated in keys

FoodRush case study (DBS/Case Study/FoodRush): 11 MongoDB query tasks, extracted in both PDF versions (rows with exam=CASE). Treat as M7 practice, not as FAT evidence.
