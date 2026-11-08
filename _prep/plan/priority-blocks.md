# Priority blocks: what exactly goes in each block

Use this file when you sit down: open the block, work the list top to bottom, tick it. P1 = Must (asked in most papers), P2 = High. Paper + question numbers for every topic are in `_prep/analysis/important-topics.html` (tab "Every topic in every paper"). Slides and page numbers are in `_prep/study-guide/`.
A block ends when its time is up. Do not extend it. Whatever is unticked goes to that subject's weak-spots block.
Start rule: 25 minutes on the first item, phone away. Then decide.

## CAD (exam Fri 13 Nov)
Answer shape for every question: requirement, services, small diagram, one line of "why" per requirement.
- **P1a Mon 9 AM**
  - [ ] VPC: public/private subnet, IGW, NAT, route tables (5 of 5 papers). Draw the standard diagram twice.
  - [ ] IAM: users, groups, roles, policies, MFA, least privilege (4/5)
  - [ ] Shared responsibility model (2/5)
- **P1b Mon 9 PM**
  - [ ] RDS Multi-AZ vs Read Replica (4/5)
  - [ ] RDS vs Aurora vs DynamoDB choice (3/5)
  - [ ] CloudWatch + CloudTrail + Config together (4/5)
- **P1c Mon 9 Eve**
  - [ ] SQS, SNS, Step Functions, SWF (4/5)
  - [ ] Snow family: Snowball, Snowball Edge, Snowmobile, when to use each (4/5)
- **P2a Tue 10 AM**
  - [ ] EC2 launch steps (9), instance types, lifecycle (2/5)
  - [ ] Auto Scaling + ELB (3/5)
  - [ ] Storage choice: S3, EBS, EFS, Glacier, lifecycle (3/5)
- **P2b Tue 10 PM**
  - [ ] KMS and encryption types (3/5)
  - [ ] WAF rules, Shield (3/5 each)
  - [ ] Cost control: Budgets, Cost Explorer, Trusted Advisor (3/5)
- **P2c Tue 10 Eve**
  - [ ] DMS + Schema Conversion Tool, Server Migration Service (3/5 each)
  - [ ] Well-Architected pillars and HA design (2/5)
  - [ ] Security group vs NACL, VPN / Direct Connect / peering, CloudFront (2/5)
  - [ ] Systems Manager + Config remediation (2/5), NIST definition and global infrastructure (2/5)
- **Wed 11 AM and PM**: two timed papers (A1'25, then G1'25), 3 hours each is too long, so do 5 questions in 90 min, then fix gaps.
- **Thu 12 AM**: close the notes, write the 6 P1 topics from memory, then pick which either/or questions you will choose (see `_prep/analysis/CAD.md`).

## OS (exam Sun 15 Nov)
- **P1a Wed 11 Eve** (numericals you already do well, keep it fast)
  - [ ] CPU scheduling: Gantt, WT, TAT (7/7)
  - [ ] Banker's algorithm and deadlock detection (7/7)
  - [ ] Disk scheduling total head movement (7/7)
  - [ ] Page replacement FIFO / LRU / Optimal (5/7)
- **P1b Thu 12 PM** (theory Must)
  - [ ] OS structure, design issues, services (7/7)
  - [ ] File allocation methods (5/7)
  - [ ] Virtualisation and hypervisors (5/7)
- **P2a Fri 13 PM** (your panic topic)
  - [ ] Critical section, Peterson, Test-and-Set (4/7)
  - [ ] Readers-writers (3/7)
  - [ ] Race condition with a worked example (3/7)
- **P2b Fri 13 Eve**
  - [ ] Barber, dining philosophers and other classics (3/7)
  - [ ] Process vs thread, PCB, states, system calls (4/7); fork() / pthreads programs (3/7)
  - [ ] Paging address bits, page-table size (3/7); fragmentation, segmentation (3/7)
  - [ ] Access matrix, ACL, capability lists (3/7)
- **Sat 14**: timed paper (AM), weak spots + semaphores again (PM), light recall (Eve).

## AI (exam Thu 19 Nov)
- **P1a Sun 15 PM**: Greedy best-first and A* on a graph (5/6); Uniform-cost search (P2, 3/6)
- **P1b Sun 15 Eve**: FOL sentences and resolution proof (5/6); forward / backward chaining (4/6)
- **P1c Mon 16 AM**: Minimax and alpha-beta (4/6); PEAS for a scenario (4/6); environment properties (P2, 3/6)
- **P1d Mon 16 PM**: Bayes theorem numericals (4/6); Bayesian network inference (4/6)
- **P1e Mon 16 Eve**: STRIPS representation / plan (5/6); HTN planning (4/6); information retrieval and ranking (4/6)
- **P2 Tue 17 AM**: DFS / BFS / IDDFS (3/6); genetic algorithm (3/6); hill climbing and simulated annealing (3/6); propositional logic rules, truth table, CNF (3/6); English to FOL (3/6)
- **Wed 18 AM**: timed paper, then fix gaps. Do not start P3 topics before this.

## DBS (exam Sun 22 Nov)
Say the word and I will teach each block step by step with your slides' notation. FDs and normalisation are the first thing to get help with.
- **P1a Tue 17 PM**: three-schema architecture and data independence (4/4); ER / EER design from a scenario (4/4); generalisation, specialisation, aggregation (3/4)
- **P1b Tue 17 Eve**: normalisation to 3NF / BCNF with FDs (4/4). Start from closure of attributes and candidate keys.
- **P1c Wed 18 PM**: B+ tree insertion and deletion (3/4); hashing: static, extendible, double hashing, probing (3/4)
- **P1d Thu 19 PM**: serializability, precedence graph, recoverability, ACID (4/4)
- **P1e Thu 19 Eve**: two-phase locking strict / rigorous (3/4); NoSQL types and CAP theorem (4/4)
- **P2a Fri 20 AM**: relational algebra queries (2/4); lossless and dependency-preserving decomposition (2/4)
- **P2b Fri 20 PM**: recovery: log-based, deferred / immediate, shadow paging (2/4); deadlock: wait-for graph, wait-die / wound-wait (2/4); timestamp ordering, Thomas write rule (2/4)
- **Fri 20 Eve and Sat 21**: mixed problems, timed paper, weak spots.

## ACC (practical Tue 24 Nov, 11:00-12:30)
No papers exist, so this is a guess from the syllabus. Warm-up every day from now: one Java program, 30 minutes, written from a blank file.
- **P1 Sun 22 PM**: Java I/O, loops and class structure; arrays (max product subarray, leaders, majority element); sieve
- **P2 Sun 22 Eve**: bit tricks and GCD; quick sort and selection sort; string problems (palindromes, weighted substring)
- **P2 Mon 23 AM**: recursion and backtracking (N-Queens, maze, permutations); activity selection and Kruskal if time

## CN (exam Thu 26 Nov)
You know most numericals, so this is mostly a fast pass with timed practice.
- **P1a Tue 24 PM**: topology and OSI / TCP-IP layers (3/3); circuit vs packet switching and delay numericals (3/3); error detection: parity, CRC, checksum, Hamming (2/3); CSMA/CD, CSMA/CA, ALOHA (2/3)
- **P1b Tue 24 Eve**: subnetting, VLSM, CIDR (2/3); IPv4 fragmentation with MTU (2/3); distance vector, count-to-infinity (2/3); link state, Dijkstra (2/3)
- **P1c Wed 25 AM**: congestion control, leaky and token bucket (2/3); DNS, HTTP, email (3/3)
- **Wed 25 PM**: timed paper + gaps. Evening: light recall.

## CD (exam Mon 30 Nov)
Order matters here because later topics build on earlier ones. All P1 are done by Fri 27 PM, with 3 days spare.
- **P1a Mon 23 PM**: phases of a compiler on a code snippet (6/7); regex to DFA by direct method (P2, 4/7)
- **P1b Mon 23 Eve**: FIRST, FOLLOW and LL(1) table (5/7)
- **P1c Thu 26 PM**: SDD / SDT, attribute grammars (7/7)
- **P1d Thu 26 Eve**: three-address code, quadruples, triples, indirect triples (6/7); backpatching (5/7)
- **P1e Fri 27 AM**: basic blocks and flow graph (7/7); identify and apply optimisation techniques (5/7)
- **P1f Fri 27 PM**: instruction scheduling, software pipelining, parallelism (6/7)
- **P2a Sat 28 PM**: LALR(1) / CLR(1) items and table (4/7); SLR(1) table and conflicts (3/7); DAG of a basic block (3/7)
- **P2b Sat 28 Eve**: register allocation (4/7); code generator design issues (3/7); Lex program, Thompson NFA (3/7)
- **Sun 29**: mixed problems, timed paper + gaps, light recall.

## Indian Constitution (exam Sat 28 Nov, 1 hour)
- **Fri 27 Eve**: one block across Weeks 1-6. Priority guess (no papers): Preamble and features, Fundamental Rights and Duties first, then DPSP, Parliament, state executive and judiciary, local government.
