# Raw topic tallies behind important-topics.html (AI, OS, DBS, CN)

Working notes written while reading the FAT papers. Subject modules follow each syllabus. CAD and CD tallies come from `pyq-index/CAD.md` and `pyq-index/CD.md`.

## AI
```
AI FAT papers (6): E1'24(Nov), E2'24(Nov), B1'24(May), D1'25, D2'25, G2'25 (G2 OCR partial). 100 marks, 10x10 (B1: any 10 of 12). Last two Qs (Q9,Q10) are OR in E1,E2,D1,D2.
2025 pattern (D1,D2): Q1 M1 PEAS/env; Q2 UCS/uninformed; Q3 GBFS+A*; Q4 minimax+alpha-beta; Q5 inference rules/chaining or GA(D2); Q6 FOL+resolution; Q7 Bayes/uncertainty; Q8 Bayes classifier/medical Bayes; Q9 planning OR (STRIPS blocks/HTN); Q10 M7 OR (IR / object recognition / NLP / IE).
Tallies (papers of 6): 
M1: PEAS 4 (B1,D1,D2,G2); env properties 3 (E2,D1,D2); agent types/architecture 2 (B1 goal-based,G2); AI classification 1 (E1); subfields 1 (D1)
M2: GBFS+A* 5 (E1,B1,D1,D2,G2); UCS 3 (E1,D1,D2); DFS/BFS/IDDFS 3 (E2,B1,D1); state-space formulation 2 (E2 hanoi,B1 river crossing); uninformed comparison table 1 (D2)
M3: minimax+alpha-beta 4 (E1,B1,D1,D2); hill climbing/SA 3 (E2,B1,G2); genetic algorithm 3 (E2,D2,G2)
M4: FOL resolution 5 (E1,B1,D1,D2,G2); fwd/bwd chaining 4 (E1,D1,D2,G2); FOL representation 3 (E2,D1,D2); propositional inference/truth table/CNF 3 (B1,E2,D1); unification 1 (D2)
M5: Bayes theorem numericals 4 (B1,E2,D1,D2); Bayesian network 4 (E1,B1,E2,G2); naive Bayes classifier 2 (E1,D1)
M6: STRIPS/plan 5 (E1,B1,D1,D2,G2); HTN 4 (E1,B1,D1,G2); fwd vs bwd planning search 2 (E2,D2); nondeterministic planning 2 (E1,B1); multiagent planning 1 (E2)
M7: info retrieval/ranking 4 (E1,E2,D1,D2 10b IE vs IR); NLP/language models 2 (B1,D2); object recognition 1 (D1); image retrieval 1 (E2)
```

## OS
```
OS FAT papers read so far (text): B1'24(Nov,10x10), B2'24(Nov,10x10), D1'26(Apr/May 2026; Sec I 4x10 + Sec II 4x15, no OR), D2'24(May; Sec I 4x10 + Sec II 4x15)
M1: OS structure monolithic/micro/layered 3 (B1 1b,B2 Q1,Q2); OS services/functions 2 (D1 Q1,D2 Q1); clustered vs multiprocessor 1 (B1)
M2: fork() output count 1 (B1); user vs kernel threads 1 (B1); thread C program (pthreads) 1 (D2); process fork/wait C program 1 (D1)
M3: CPU scheduling Gantt/WT/TAT 4/4 (B1 RR+SRTF/priority OR, B2 SJF+Prio+RR, D1 priority pre/non-pre, D2 FCFS+RR); Banker's/deadlock detection/recovery 4/4 (B1 Q4, B2 Q4, D1 RAG->WFG, D2 Q5)
M4: classic sync problems 4/4 but different each time: B1 readers-writers (OR desks+lamps resource), semaphore value + critical-section 2-process method; B2 race condition banking; D1 monitor producer-consumer; D2 barber problem
M5: page replacement FIFO/LRU/OPT 3/4 (B2,D1 w Belady,D2); multilevel paging address bits 1 (B1); TLB EMAT 1 (B1); first/best/worst fit 1 (B1); fragmentation 2 (B1,B2)
M6: file allocation methods 3 (B1,D1,B2 9b OR); virtualization 2 (B2,D2); directory structures 1 (B2 9a OR); file retention policy 1 (D2)
M7: disk scheduling 4/4 (B1,B2,D1,D2); capability-based systems 1 (B2 10b OR)
--- FINAL OS (7 FAT papers: B1'23 Jul2023, B1'24, B2'24, D2'24 May, C1'25, C2'25, D1'26 Apr/May). Q order: Q1 M1, Q2 M2, Q3 sched, Q4 Banker, Q5-6 sync, Q7-8 memory, Q9 M6, Q10 M7; OR in last 2-3 Qs in B2'24, C1'25 (Q9,Q10), C2'25 (9a/b paging vs address calc; ACL vs virtualization), B1'24 (Q3,Q5).
M1 OS structure/design issues/services/dual mode: 7/7
M2 threads vs process/PCB/system calls: 6/7 (B1'23,B1'24,C1,C2,D2 pthread prog,D1 fork prog); fork() output count 1 (B1'24)
M3 CPU scheduling Gantt/WT/TAT: 7/7 (FCFS,SJF,SRTF,RR,priority); Banker's/safe state/RAG-WFG/recovery: 7/7
M4 sync: 7/7. critical-section conditions/Peterson/TSL 4 (B1'23,B1'24,C1,C2); readers-writers 3 (B1'23,B1'24,C1); producer-consumer/monitor 2 (C2,D1); race condition 2 (B2,C1); barber 1 (D2); semaphore-value tracing 2 (B1'23,B1'24)
M5 page replacement FIFO/LRU/OPT 5/7 (B1'23,B2,D2,C1,D1 w Belady); paging address bits/page table size 4 (B1'24,C1,C2 x2); TLB EMAT 2 (B1'23,B1'24); first/best/worst fit 2 (B1'23,B1'24); fragmentation 2; page table structures 1 (C1)
M6 file allocation 6/7 (B1'23,B1'24,B2,C2,D1,C1 free-space); virtualization/hypervisors 5/7 (B1'23,B2,D2,C1 Type1/2,C2); directory structures 1; free-space mgmt 1
M7 disk scheduling FCFS/SSTF/SCAN/LOOK/C-SCAN 7/7; access matrix/capability/ACL 3 (B2,C1,C2)
```

## DBS
```
DBS FAT (12 papers; read in detail: A1'24-25(key), A2'24-25, E1'25-26, B2'25-26, plus fragments A2'24, A2'22-23, F2'23-24; scanned A1'23-24,B2'22-23,B2'24-25 keyword-only; B1'25-26 image not read). 100 marks, 10x10; module order. Q1 M1 three-schema (always Q1, 4/4 read). Q2 ER/EER design (4/4; with specialization/aggregation). Q3-Q4(-Q5) M3 FDs: minimal cover/Armstrong derivation (E1), FD equivalence + candidate keys (A2), dependency preservation/lossless decomposition (A1,A2), anomalies + 3NF/BCNF normalization (A1,E1,B2,A2'24 BCNF) -> 4/4. Q5-Q6 M4: B+ tree insert/delete (A1,A2 OR,E1) 3/4 (+B2 multilevel indexing), hashing: static+quadratic probing (E1), double hashing (A1), extendible (A2) 3/4; sparse vs dense (A2'24); relational algebra queries (A2'24-25, B2'25, A2'22,F2'23). Q6-Q7 M5: recovery log-based UNDO/REDO/shadow (A1,E1) ; conflict serializability/precedence graph/recoverable/cascadeless (A2,E1,B2,A1 Q7) 4/4; ACID scenarios (A2). Q8-Q9 M6: 2PL types/strict 2PL (A1 Q10, A2 Q9, E1 Q8b, B2) 4/4; deadlock WFG/prevention (A2 Q8,E1 Q8a) 2; timestamp ordering basic+Thomas write rule (E1 Q9, A1) 2; multi-granularity locking (B2 Q9b). Q10 M7 NoSQL always: CAP theorem (A1 Q8, B2 10a OR), NoSQL types/which suits (A2 Q10, E1 Q10, B2 10b OR). OR seen only in B2'25-26 (Q10) and A2'24-25 (Q5 a/b).
```

## CN
```
CN FAT (12 papers; read in detail A1'25-26 (Q1-7), F2'25-26, D1'24; rest keyword-only; F1'25-26 image unread). 10x10, module order. Q1 topology/OSI (M1), Q2 circuit vs packet switching + delay calc (M2), Q3 error detection (parity/CRC/Hamming) (M3), Q4 CSMA/CD/CA/ALOHA/wireless (M3), Q5-6 OSI-layers scenario / switching latency / ARQ stop-and-wait (M3), subnetting/VLSM + IPv4 fragmentation/MTU (M4), IPv4 vs IPv6/NAT (M4), distance vector + count-to-infinity / link state (M5), congestion open/closed loop + leaky/token bucket / TCP (M6), DNS caching / HTTP headers / SMTP (M7).
```
