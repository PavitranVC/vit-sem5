# CD (BCSE307L Compiler Design): FAT pattern report for slot G2

Machine-readable: `patterns.json`. Raw numbers: `analysis_raw.json`. Rows: `questions.csv`, `questions_text.jsonl`.
**O** = observed (counted), **I** = inferred (rule or judgement). Every claim cites file:Qn.

## 1. Data and validation

| item | value |
|---|---|
| question rows (all codes) | 234 |
| distinct BCSE307L papers (QP/AK duplicates merged by text similarity >= 0.6) | 24: 7 FAT (0 from 2026-27), 9 CAT-1, 8 CAT-2 (O) |
| 2026-27 sister-course FATs | 0: none (O) |
| orchestrator re-read | 14 questions re-read (BCSE307L-CAT2-G2-2026-2027 Q1-Q5b, BCSE307L-CAT1-G2-2026-2027 Q1-Q5): text 14/14, type 10/14, bloom 13/14, scenario wrapper 2/14; pooled 25/42 = 0.60. Scenario-wrapper tags are unreliable for CD (extractors counted code listings, grammars and 'Assume...' blocks as narrative). (O) |
| marks check | 5 papers flagged (unprinted per-question marks, OR alternatives, case-study items); see validation.md (O) |
| rows with ocr_flag=1 | 57 (O) |
| backtest confidence (OS+AWS) | Medium: 22 of 40; naive frequency list 22 of 40 (O) |

## 2. FAT blueprint (O)

10-question FATs (A2 2023-24 and E1 2025-26 have 8-9 numbered questions with sub-parts); all 7 modules in 4 of 7 FATs, 6 modules in the other 3. Order is roughly syllabus order (Q1-Q2 M1 phases/lexical, Q3-Q4 M2 parsing, then M3 SDT, M4 intermediate code, M5 optimisation, M6 code generation, M7 parallelism) but shuffled in E1 2025-26 and C1 2024; 'Q9 a or b; Q10 a or b' in 3 of 7. No 2026-27 BCSE307L FAT in the corpus; 2026-27 evidence = CAT-1 G1, CAT-1 G2 and CAT-2 G2 (your slot).

## 3. Ranked topics for slot G2

p = (2k_recent + k_older + 1)/(2n_recent + n_older + 2) over BCSE307L FATs (n_recent=0, n_older=7). 'all' = CAT/FAT papers covering the module.

| rank | topic | mod | p (FAT) | FAT ratio | p (all) | all ratio | 2026-27 CATs (of 3) | 2026-27 sister FATs (of 0) | core type | example (fluff stripped) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SDD / SDT / annotated parse tree | M3 | 0.89 | 7 of 7 | 0.83 | 14 of 15 | 0 | 0 | trace | Design SDD generating prefix form with type checking and type promotion [printed CO3/K3] (cite BCSE307L-FAT-E1-2025-2026:Q1a) |
| 2 | Phases of compiler | M1 | 0.78 | 6 of 7 | 0.90 | 15 of 16 | 2 | 0 | trace | Explain how analysis and synthesis phases process the discriminant statement. (cite BCSE307L-CAT1-G1-2026-2027:Q1) |
| 3 | Three-address code / quadruples / triples | M4 | 0.78 | 6 of 7 | 0.83 | 13 of 15 | 1 | 0 | trace | Generate TAC for nested loops with break, quadruples and triples for sum computation, and decide placement of result statement. (cite BCSE307L-CAT2-G2 |
| 4 | Code generation / register allocation | M6 | 0.78 | 6 of 7 | 0.78 | 6 of 7 | 0 | 0 | theory | Explain issues in code generation phase with an example for each [CO5/K2] (cite BCSE307L-FAT-E1-2025-2026:Q4) |
| 5 | Code optimization (CSE/constant folding/loop) | M5 | 0.78 | 6 of 7 | 0.78 | 6 of 7 | 0 | 0 | theory | Identify all applicable optimizations in a C snippet and write the fully optimized code [CO5/K3] (cite BCSE307L-FAT-E1-2025-2026:Q2) |
| 6 | Basic blocks / flow graph | M4 | 0.78 | 6 of 7 | 0.67 | 10 of 15 | 1 | 0 | trace | Generate numbered TAC, find leaders, partition into basic blocks, justify block boundary for a=a+2. (cite BCSE307L-CAT2-G2-2026-2027:Q5b) |
| 7 | Instruction scheduling / ILP | M7 | 0.67 | 5 of 7 | 0.67 | 5 of 7 | 0 | 0 | theory | Explain role and significance of instruction scheduling with examples. (cite BCSE307L-FAT-A1-2025-2026:Q8) |
| 8 | Backpatching | M4 | 0.67 | 5 of 7 | 0.56 | 9 of 15 | 0 | 0 | trace | Explain backpatching for given if-else with compound condition. (cite BCSE307L-FAT-A1-2025-2026:Q10b) |
| 9 | CLR / LALR parsing | M2 | 0.67 | 5 of 7 | 0.48 | 12 of 24 | 1 | 0 | trace | Build canonical LR(1) sets, ACTION/GOTO, decide CLR(1), explain e-reduction conflict, trace parse of switch(x){case 1:y=z;}. (cite BCSE307L-CAT2-G2-20 |
| 10 | Direct RE to DFA | M1 | 0.56 | 4 of 7 | 0.80 | 13 of 16 | 2 | 0 | trace | Direct-method DFA for (a+e+b)* a* b+ a # with syntax tree, firstpos/lastpos, followpos, transition table. (cite BCSE307L-CAT1-G1-2026-2027:Q2) |
| 11 | Syntax tree / DAG | M4 | 0.56 | 4 of 7 | 0.50 | 7 of 15 | 1 | 0 | trace | Construct DAG for 10-statement basic block, value numbers, identify common subexpressions and d's node. (cite BCSE307L-CAT2-G2-2026-2027:Q2a) |
| 12 | LL(1) parsing table | M2 | 0.56 | 4 of 7 | 0.45 | 11 of 24 | 1 | 0 | trace | Compute FIRST/FOLLOW, LL(1) table, and trace parse of xx+zz?. (cite BCSE307L-CAT1-G2-2026-2027:Q4) |
| 13 | LR(0) / SLR parsing | M2 | 0.56 | 4 of 7 | 0.45 | 10 of 24 | 2 | 0 | trace | Build canonical LR(0) collection and SLR(1) table; parse cabbab. (cite BCSE307L-CAT1-G1-2026-2027:Q5) |
| 14 | Tokens / lexemes / LEX | M1 | 0.44 | 3 of 7 | 0.40 | 7 of 16 | 0 | 0 | theory | Write a Lex program that checks and displays whether input contains digits, alphabets or special characters [CO1/K2] (cite BCSE307L-FAT-E1-2025-2026:Q |
| 15 | FIRST / FOLLOW | M2 | 0.44 | 3 of 7 | 0.24 | 5 of 24 | 1 | 0 | numerical | Compute FIRST/FOLLOW, build LL(1) table, decide with justification if G is LL(1), locate conflicts. (cite BCSE307L-CAT1-G1-2026-2027:Q4) |
| 16 | Loop parallelism | M7 | 0.33 | 2 of 7 | 0.33 | 2 of 7 | 0 | 0 | theory | Identify the most likely candidate in the code for parallelization and explain why (cite BCSE307L-FAT-E1-2025-2026:Q7c) |
| 17 | S-attributed / L-attributed | M3 | 0.33 | 2 of 7 | 0.22 | 3 of 15 | 0 | 0 | theory | Differentiate synthesized and inherited attributes with examples. (cite BCSE307L-FAT-A2-2025-2026:Q4ii) |
| 18 | Recursive descent | M2 | 0.33 | 2 of 7 | 0.21 | 5 of 24 | 0 | 0 | trace | Eliminate left factoring and write recursive descent functions for transformed grammar. (cite BCSE307L-FAT-A1-2025-2026:Q9b) |
| 19 | Symbol table | M3 | 0.33 | 2 of 7 | 0.17 | 2 of 15 | 0 | 0 | trace | Draw activation record, explain its fields, and draw memory layout for fact(4) and fact(2). (cite BCSE307L-FAT-A1-2025-2026:Q7) |
| 20 | Operator precedence parsing | M2 | 0.22 | 1 of 7 | 0.31 | 7 of 24 | 1 | 0 | trace | Build operator-precedence table and parse id and (id or id) showing stack and input. (cite BCSE307L-CAT1-G2-2026-2027:Q3) |
| 21 | Type checking | M3 | 0.22 | 1 of 7 | 0.22 | 2 of 15 | 1 | 0 | theory | Do semantic type analysis of array references, derive row-major addresses and combined bounds condition on i and j. (cite BCSE307L-CAT2-G2-2026-2027:Q |
| 22 | Data-flow analysis | M5 | 0.22 | 1 of 7 | 0.22 | 1 of 7 | 0 | 0 | trace | Draw DFG, dominator tree, loops and back edges, apply constant propagation, identify loop invariants at lines 8 and 16. (cite BCSE307L-FAT-C1-2023-202 |

Teach order (I): tier p >= 0.75 by module, then 0.50-0.75, then the rest (`teach_order`).

## 4. Drift: 2026-27 vs older (O; small n)

| exam | group | papers | mean Bloom | scenario wrapper % q | theory % marks | (num+trace):theory |
|---|---|---|---|---|---|---|
| CAT1 | older | 7 | 3.36 | 6.4 | 4.5 | 21.0 |
| CAT1 | recent_2026_27 | 2 | 3.1 | 50.0 | 10.0 | 9.0 |
| CAT2 | older | 7 | 3.23 | 14.0 | 21.5 | 3.65 |
| CAT2 | recent_2026_27 | 1 | 3.22 | 88.9 | 0.0 | None |
| FAT | older | 7 | 3.24 | 18.0 | 35.4 | 1.75 |
| all | scenario wrapper % by start year | 2023: 9.0, 2024: 13.2, 2025: 19.2, 2026: 68.4 | | | | |

Bloom: 2026-27 CAT-1 mean 3.10 vs 3.36 older; CAT-2 3.22 vs 3.23 (O). Scenario-wrapper figures are excluded (verification 2/14). 2026-27 G2 CAT-2 questions are long multi-part prompts that ask for a justification after the construction (Q1, Q2a, Q3c, Q4: O).

## 5. Slot pairs and sister courses (I: rule-based matching)

| comparison | n q | Identical | Same concept new numbers | Same module only | Unrelated |
|---|---|---|---|---|---|
| slot 1 -> slot 2, same exam+year (8 pairs) | 70 | 0.0 | 0.514 | 0.443 | 0.043 |
| different letter, same year (11 pairs) | 121 | 0.008 | 0.595 | 0.339 | 0.058 |
| baseline: same exam, different year (132 pairs) | 1199 | 0.003 | 0.585 | 0.382 | 0.029 |

Slot 1 -> slot 2 shares the archetype for 0.51 of questions vs 0.58 between different years (O): no slot rule. No verbatim reuse in 2026-27 (max similarity 0.54).

## 6. Answer keys: what earns marks (O)

44 key rows; step marks stated in 7; penalties stated in 0.

| topic | mandatory elements from real keys |
|---|---|
| SDD / SDT / annotated parse tree | key shows: S.val = S1.val * T.val [BCSE307L-CAT2-A1-2025-2026-AK:Q2a]<br>key shows: parse tree for the expression 20 # 10 % 5 # 8 % 2 % 2 [BCSE307L-CAT2-A1-2025-2026-AK:Q2c] |
| Phases of compiler | key shows: lexical tokens; syntax tree; semantic check; intermediate code; optimization; code generation [BCSE307L-CAT1-A1-2025-2026-AK:Q1]<br>key shows: tokens; parse tree/AST; semantic checks; three-address code; optimization; machine code [BCSE307L-CAT1-A2-2025-2026-AK:Q1] |
| Three-address code / quadruples / triples | marks: SDT to generate intermediate code 2; backpatching explanation 2; key shows: quadruples; triples; indirect triples; label L2; backpatching for forward jumps [BCSE307L-CAT2-A1-2025-2026-AK:Q3]<br>marks: three-address code 4; key shows: labels L1..; conditional gotos; count++; s = sqrt(n); inner loop j=2*i [BCSE307L-CAT2-A1-2025-2026-AK:Q5a] |
| Code optimization (CSE/constant folding/loop) | key shows: Common Subexpression Elimination; Loop-Invariant Code Motion; Strength Reduction; Induction Variable Optimization; Copy Propagation [BCSE307L-CAT2-A2-2025-2026-AK:Q5]<br>key shows: loop unrolling; reduced loop control overhead; time complexity O(n^3); space unaffected [BCSE307L-CAT-2-C2-2024-2025-Answer Key:Q5b] |
| Basic blocks / flow graph | marks: basic blocks 3; key shows: leaders; basic block boundaries [BCSE307L-CAT2-A1-2025-2026-AK:Q5b]<br>marks: flow graph 3; key shows: flow graph edges between basic blocks [BCSE307L-CAT2-A1-2025-2026-AK:Q5c] |
| Backpatching | key shows: true list; false list; back patch table; labels L2-L9, Lend [BCSE307L-CAT2-A2-2025-2026-AK:Q4]<br>key shows: truelist; falselist; backpatch; goto targets; param/call printf [BCSE307L-CAT-2-C2-2024-2025-Answer Key:Q3] |
| CLR / LALR parsing | marks: Representation of canonical LR(1) items 3; parsing table 3; justification and parse trace 2 plus 2; key shows: productions Stmt->DeclStmt, DeclStmt->Type IdList ;, Type->char, IdList->identifier IdListTail, IdListTail->, identifier IdListTail, IdListTail->e; LR(1) item s [BCSE307L-CAT2-A1-2025-2026-AK:Q1]<br>key shows: LR(1) items I0-I12 with lookaheads {$} and {end}; LR(1) parsing table; DFA diagram; stat'->.stat,{$} [BCSE307L-CAT2-A2-2025-2026-AK:Q1] |
| Direct RE to DFA | key shows: augmented regex with end marker; firstpos/lastpos/followpos; DFA states; accepting states [BCSE307L-CAT1-A1-2025-2026-AK:Q2]<br>key shows: regex a?(ab)*b?; positions numbered; firstpos/lastpos/followpos sets [BCSE307L-CAT1-A2-2025-2026-AK:Q2] |
| Syntax tree / DAG | key shows: newNode; newLeaf; E.node/T.node/F.node; * and / nodes under - root [BCSE307L-CAT-2-C2-2024-2025-Answer Key:Q2b] |
| LL(1) parsing table | key shows: FIRST and FOLLOW sets; parsing table; left recursion removal for B; stack trace for abbc [BCSE307L-CAT1-A1-2025-2026-AK:Q4] |
| LR(0) / SLR parsing | key shows: augmented grammar S'->S; states I0-I5; FOLLOW(S)={+,*,$}; action table [BCSE307L-CAT1-A2-2025-2026-AK:Q5]<br>key shows: augmented grammar; LR(0) item sets I0-I8; FOLLOW(E)={$,=}; SLR action and goto table; shift-reduce stack trace [BCSE307L-CAT-2-C1-2024-2025-Answer Key:Q1] |
| S-attributed / L-attributed | key shows: B.val=0/1; Y.val=Y1.val*2+B.val; Y.len=Y1.len+1; X.val=Y1.val+(Y2.val/(2^Y2.len)); X.val=Y.val [BCSE307L-CAT2-A2-2025-2026-AK:Q2a] |
| Recursive descent | key shows: left recursion removal; left factoring; procedures A, A', B, B', C, C'; match and error calls [BCSE307L-CAT1-A1-2025-2026-AK:Q3a]<br>key shows: stepwise derivation; string not parsed at the point where no rule applies [BCSE307L-CAT1-A1-2025-2026-AK:Q3b] |
| Operator precedence parsing | key shows: precedence relation table; precedence functions f and g; shift/reduce trace; stack and input columns [BCSE307L-CAT1-A1-2025-2026-AK:Q5]<br>key shows: precedence of % over #; left associativity of both [BCSE307L-CAT2-A1-2025-2026-AK:Q2b] |
| Peephole optimization | key shows: redundant instruction removal; algebraic simplification; use machine idioms; unreachable code removal; flow of control optimization [BCSE307L-CAT-2-C1-2024-2025-Answer Key:Q5b] |
| Ambiguous grammar | key shows: leftmost derivation; rightmost derivation; parse tree; ambiguity argument [BCSE307L-CAT1-A2-2025-2026-AK:Q3a]<br>key shows: leftmost derivation; rightmost derivation; parse tree; unambiguity argument [BCSE307L-CAT1-A2-2025-2026-AK:Q3b] |
| Left recursion / left factoring | key shows: left recursion elimination; left factoring cA X; shift-reduce table; stuck state S+ [BCSE307L-CAT1-A2-2025-2026-AK:Q4] |

## 7. Observed traps

- Three-address code / quadruples / triples: Decide from the braces whether result = sum + i*2 runs per inner iteration, per outer iteration or once; quadruples/triples only for the conditional sum part [BCSE307L-CAT2-G2-2026-2027:Q4]
- Basic blocks / flow graph: Decide whether a = a + 2 and b = b - 1 share a block with the result > 100 test using leader rules; no CFG or optimisation asked [BCSE307L-CAT2-G2-2026-2027:Q5b]
- Backpatching: Testing c != d before a < b may keep the final value but breaks left-to-right short-circuit order and side effects [BCSE307L-CAT2-G2-2026-2027:Q3c]
- CLR / LALR parsing: Asked which LR(1) item's lookahead lets Cases -> epsilon reduce only at the right place, and what conflict appears if that reduction were entered under all terminals [BCSE307L-CAT2-G2-2026-2027:Q1]
- Direct RE to DFA: Augment the expression with the end marker # and number positions before firstpos/lastpos/followpos [BCSE307L-CAT1-A1-2025-2026-AK:Q2]
- Syntax tree / DAG: b + c in statements 1 and 7 is NOT a common subexpression once b is redefined in statement 6; the question asks which occurrence cannot share the node [BCSE307L-CAT2-G2-2026-2027:Q2a]
- LL(1) parsing table: Left recursion must be removed before FIRST/FOLLOW; key removes it for B [BCSE307L-CAT1-A1-2025-2026-AK:Q4]
- LR(0) / SLR parsing: SLR reduce entries go under FOLLOW of the head only (key: FOLLOW(E) = {$, =}) [BCSE307L-CAT-2-C1-2024-2025-Answer Key:Q1]

## 8. No clear pattern

- Slot-pair reuse: slot 1 -> slot 2 same-archetype 0.51 vs different-year baseline 0.58 (70 questions): slot pairing gives no lift
- Scenario-wrapper drift: tags unreliable for CD (2/14 agreement)
- Exact FAT question order (shuffled in 2 of 7)
- M7 parallelism question type (ILP vs loop parallelism vs legacy-code parallelisation all occur)


