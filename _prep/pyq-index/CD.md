# CD (BCSE307L Compiler Design) FAT papers: raw question index (NO analysis yet)

Module key (from syllabus): M1 Intro/Lexical (phases, regex->DFA direct, Lex) | M2 Syntax (LL1, SLR/CLR/LALR, op-precedence, RDP) | M3 Semantics (SDD/SDT) | M4 Intermediate code (TAC, quad/triple, backpatching) | M5 Optimization (basic blocks, flow graph, DAG, peephole, dataflow, loops) | M6 Code generation (reg alloc, activation records, codegen issues) | M7 Parallelism (instr scheduling, software pipelining, vectorization, parallelization)

All papers: 3 hrs, 100 marks. Note: text of some papers was OCR-garbled; grammars marked (?) may have small errors.

## P1: FAT Nov 2024, slot C1+TC1 (10 x 10)
1. M1 phases of compiler, output of each phase for factorial function
2. M2 check LALR(1): S->aBc|bCc|aCd|bBd, B->e, C->e
3. M4 backpatching actions for boolean grammar (OR/AND/not/relop); TAC for a==b AND (c==d OR e==f) and (a==b AND c==d) AND e==f
4. M4 3AC + quadruple/triple/indirect triple for while loop with a[i]=0, i=i+1
5. M5 basic blocks + flow graph + loops (prime-counting sieve code)
6. M5 DAG for 12-line TAC basic block + peephole optimization
7. M6 register allocation by graph coloring on given flow graph (live sets given)
8. M7 instruction scheduling + software pipelining, examples, significance
9a. M2 remove left recursion/common prefix in if/while/begin-end grammar; FIRST/FOLLOW; LL(1) table; is it LL(1)? (OR) 9b. M2 recursive descent parser for S->^SY|^Y (?)
10a. M3 SDD to determine type of E->E+T|T, T->num.num|num; extend to postfix with inttoreal (OR) 10b. M3 SDT for syntax tree of desk calculator; evaluate 2+4*5^2

## P2: FAT Jul 2023, slot C2+TC2 (10 x 10)
1. M1 regex (a|b)*cc(d|c)* -> DFA by direct method (syntax tree, firstpos/lastpos/followpos); test "aabccd", "acdd"
2a. M1 [7] phases for if(x>5){y=x+2;}else{y=x-2;} 2b. M1 [3] Lex program counting vowels
3. M2 S->AB, A->aAb|e, B->bB|C : FIRST/FOLLOW [3], LL(1) table [5], parse "aabc" [2]
4. M2 check LALR(1): S->aAc|bCc|aCd|bAd, A->e, C->e
5a. M3/M4 [5] SDT -> TAC for E->E+T|T, T->T*F|F, F->(E)|id; annotated parse tree, input 2+3*4. 5b. [5] short-circuit evaluation of (A&&B)||(C||D) with A=T,B=F,C=T,D=F
6a. M4 [7] backpatching for A>B AND (C<D OR E!=F) 6b. [3] syntax tree for X*(Y-5)+(Z/sqrt?) (?)
7. M5 basic blocks + CFG for if/else C program (x>y, sum/difference printf)
8a. M5 [5] peephole opt on LOAD/MUL/ADD/STORE/JMP loop 8b. M5 [5] loop optimization (loop unrolling) with example
9a. M6 [5] main challenges in code generator design 9b. M6 [5] register allocation, 3 registers, int a=5,b=10,c=a+b,d=c*2,e=d/3
10a. M7 [4] what is parallelization, types of techniques 10b. M7 [6] techniques for instruction-level parallelism

## P3: FAT Nov 2025, slot A1+TA1 (10 x 10; Q9, Q10 have OR options)
1. M1 regex ((10)+(((10)+1)*1*))010 (as written) -> DFA, direct method
2. M1 phases of compiler for: a=5,b=10; if(a<b){c=a*b+(a+b)*(a+b);}
3. M2 construct LALR parser for S->X$, X->Ma|bMc|dc|bda, M->d; parse "bdc", parse tree
4a. M3 [6] SDT to parse 3*4+2+1 with E->E OP E|(E)|N, OP->+|-|*, N->1|2|3|4. 4b. M5 [4] DAG for (a/10+(b-10))*(a/10+(b-10))
5. M5 what is a basic block; convert stack push/pop program (loop i<=10, choice%3) to flow graph
6. M5 optimization techniques using Check() example (constant folding, loop-invariant, strength reduction, etc.)
7. M6 activation record structure (actual params, locals, return address, access link, control link) + memory layout for fact(4) and fact(2)
8. M7 role of instruction scheduling, examples, significance
9a. M2 LR parsing table + parse "id * [id]" for A->BC, C->e|+A, B->DE, E->e|*B, D->id|[A] (OR) 9b. M2 eliminate left factoring in S->iEtSS'|a|id:=E, S'->eS|e, E->b|b+E|b*E|(E); write recursive descent functions
10a. M4 TAC + quadruple + triple for (V1+V2)*(F1+F2)+(V1*F1/P)*F2+90 (OR) 10b. M4 backpatching for if(a==b && b<=c || a>=b+c) x=y+z else x=y-z

## P4: FAT May 2024 (Winter 2023-24), slot A2+TA2 (Sec I 7 x 10, Sec II 2 x 15)
1. M2 check LL(1): R->R#|#R|RR|R%|(R)|a|b (8 + 2 justify)
2. M2 canonical LR(1) items + parsing table [7] for BLOCK->{BODY}, BODY->{BODY STMT}|STMT, STMT->x|y; parse action [3]
3. M3 SDT for int/double declarations with array types: annotated parse tree [6] for "int a,b; double [4][3] x;", dependency graph [2], symbol table [2]
4. M4 TAC [4] + quadruple/triple/indirect triple [6] for string using binary ops @,#,$ and unary % grammar
5. M4 backpatching TAC [5] + annotated parse tree [5] for while(i<10) if (a<6)&&(b>i) a=a+i; i=i+1
6. M5/M6 DAG + optimized TAC [4]; machine code [4]; activation tree for main/average/sum [2]
7. M7 instruction scheduling + software pipelining impact [5]; vectorizing compiler vector operations [5]
8. [15] M1 regex (digit)*.digit(E|e)(+|-)(digit)*: firstpos/lastpos/followpos [6], DFA direct [6], simulate "25.4E+18" [3]
9. [15] M4/M5 for loop code (p=3.14, c=2*p*a[i], a=p*a[i]^2): TAC [4], basic blocks + flow graph [6], optimizations + optimized TAC [5]

## P5: FAT Nov 2025, slot A2+TA2 (10 x 10; Q9, Q10 have OR options)
1. M1 syntax tree for augmented regex (a*b(ba*b+ab*a)*)#; firstpos/lastpos, followpos, DFA
2a. M1 [7] trace phases for factorial loop code 2b. M1 [3] identify tokens + count total tokens in sum/arr loop code
3. M2 LL parser for expr/expr_tail/term/term_tail/factor grammar; parse (a+b)*c with parse tree
4(i). M3 [7] translation scheme building tree + post-order evaluation for "2*3+4" with S->ER, R->*ER|e, E->F+E|F, F->(S)|id (ii) [3] synthesized vs inherited attributes with examples
5. M5 nested for loops (adjacent swap / bubble sort): TAC, leaders, basic blocks, CFG
6. M5 identify all optimization techniques in computeSum/main C program, write fully optimized code
7. M6 issues in code generation phase with examples
8. M6 register allocation and assignment approaches, compare/evaluate
9a. M4 TAC + triples + indirect triples for if(c[i]!=0) a[i]=a[i]+b[i]/c[i]; else b[i]=b[i]; + advantages (OR) 9b. M4 SDT with backpatching for flow control; apply to while a<b do if c<d then X=y+z else X=y-z; annotated parse tree
10a. M2 SLR(1) table for class grammar (S->P F class I X Y ...), is it SLR(1)? conflicts (OR) 10b. M2 operator precedence table [5] for S->x=E, E->E+T|E-T|T, T->T*F|F, F->(E)|x|y|0|1; parse x=y+1*x [5]

## P6: FAT Jul 2023, slot C1+TC1 (10 x 10)
1a. M1 [5] which regexes are ambiguous (3 given) 1b. M1 [5] Thompson NFA for ((ab)*U(bc)*)ab
2. M1 phases for a=(b*c)+(c-d)/f
3. M2 Java-class declaration grammar (C->PF class identifier XY, etc): FIRST, FOLLOW, LL(1) predictive table with production numbers
4a. M2 [5] are SLR(1) and LR(1) parser behaviors identical for all strings (S->id[E]:=E, E->E+T|T, ...) 4b. M2 [5] SLR(1) stack space O(n) vs O(1) for A->Aa|e vs A->aA|e on a^n
5. M3 attributed grammar checking foreach loop id not modified in body (S/L-attributed); stack-based evaluation of L-inherited attrs
6. M3 translation scheme to check if binary tree (num BinTree1 BinTree2) is ordered
7. M4 3AC for switch(a+b) with cases (short-circuit in case 2; a[40][40], width 4; nested for loops)
8. M5 for 18-line TAC: DFG, dominator tree + loops/back edges, constant propagation, are lines 8 and 16 loop invariant?
9a. M6 [5] machine code from register assignment + DAG for basic block (read a,b; c=a+b; d=a-b; ...; print e) 9b. M5 [5] copy propagation + dead code elimination on 14-line TAC (t1=j-1 ... A[t11]=temp)
10. M7 short notes: instruction scheduling, software pipelining

## P7: FAT Apr/May 2026 (Winter 2025-26), slot E1+TE1 (Sec I 4 x 10, Sec II 4 x 15)
1. M3 [10] design SDD generating prefix form + type checking with promotion; annotated parse tree for (a+b)*(c-d/e)
2. M5 [10] identify all code optimizations in given C snippet (a=b+c; x=b+c; y=a+x; if(y==2*a)... result=(d*0)+5 ...), write fully optimized code
3. M4 [10] TAC + quadruples + triples for (T1+T2)+(P1-P2)+(T1+P1/K)+100
4. M6 [10] issues in code generation with examples
5a. M1 [10] which compiler phase detects each of 5 errors (undeclared var, invalid operator, missing semicolon, type mismatch, chained assignment) 5b. M1 [5] Lex program to classify input as digits/alphabets/special chars
6. M2 [15] SLR for query grammar Q->select L from id where C, L->L,id|id, C->C and C|id<id|id>id: LR(0) canonical collection [6], FOLLOW [3], SLR table + conflicts [6]
7. M7 [15] case study: serial Fortran weather simulation: reasons serial inadequate, why faster CPU won't help, parallelization candidate, automatic parallelization of loops, risks on legacy code
8. M4/M5 [15] queue-insert code (for i=1..5, front/rear): TAC [5], leaders + basic blocks [5], CFG [5]
