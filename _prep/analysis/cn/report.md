# CN (BCSE308L Computer Networks): FAT pattern report for slot F2

Machine-readable: `patterns.json`. Raw numbers: `analysis_raw.json`. Rows: `questions.csv`, `questions_text.jsonl`.
**O** = observed (counted), **I** = inferred (rule or judgement). Every claim cites file:Qn.

## 1. Data and validation

| item | value |
|---|---|
| question rows (all codes) | 618 |
| distinct BCSE308L papers (QP/AK duplicates merged by text similarity >= 0.6) | 31: 11 FAT (0 from 2026-27), 11 CAT-1, 9 CAT-2 (O) |
| 2026-27 sister-course FATs | 2: BACSE203-FAT-B1-2026-2027, CBS3001-FAT-C2-2026-2027 (O) |
| orchestrator re-read | 13 questions re-read (BCSE308L-FAT-F2-2025-2026 Q1a-Q6iv, pages 1-2): text 13/13, type 13/13, bloom 11/13, scenario 9/13; pooled 33/39 = 0.85. (O) |
| marks check | 8 papers flagged (unprinted per-question marks, OR alternatives, case-study items); see validation.md (O) |
| rows with ocr_flag=1 | 53 (O) |
| backtest confidence (OS+AWS) | Medium: 22 of 40; naive frequency list 22 of 40 (O) |

## 2. FAT blueprint (O)

10 x 10 FAT in 9 of 11 (C2 2022-23 and A1 2025-26 printed 11-13 numbered questions); all 7 modules in 10 of 11. Typical order Q1 M1 (layers/topologies), Q2 M2 (switching/delay), Q3-Q4 M3 (error detection, MAC, flow control), Q4-Q6 M4 (IPv4 subnetting, fragmentation), Q6-Q7 M5 (routing), Q7-Q9 M6 (congestion, TCP), Q8-Q10 M7 (application layer). Your slot letter's last FATs (F1, F2 2025-26) moved M3 to Q9-Q10. No 2026-27 BCSE308L FAT in the corpus; 2026-27 evidence = CAT-1/CAT-2 C1 and C2 plus sister FATs BACSE203 B1 and CBS3001 C2.

## 3. Ranked topics for slot F2

p = (2k_recent + k_older + 1)/(2n_recent + n_older + 2) over BCSE308L FATs (n_recent=0, n_older=11). 'all' = CAT/FAT papers covering the module.

| rank | topic | mod | p (FAT) | FAT ratio | p (all) | all ratio | 2026-27 CATs (of 4) | 2026-27 sister FATs (of 2) | core type | example (fluff stripped) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IPv4 addressing / subnetting / CIDR | M4 | 0.92 | 11 of 11 | 0.96 | 20 of 20 | 2 | 2 | numerical | For 205.80.60.0 split into 5 subnets, find hosts per subnet, subnet address, first/last host, direct/limited broadcast, subnet mask. (cite BCSE308L-CA |
| 2 | Circuit vs packet switching | M2 | 0.77 | 9 of 11 | 0.89 | 20 of 22 | 2 | 1 | theory | Evaluate circuit vs packet switching for hospital operation-theatre communication and recommend one with justification. (cite BCSE308L-CAT1-C1-2026-20 |
| 3 | MAC (ALOHA/CSMA/CD/CA) | M3 | 0.77 | 9 of 11 | 0.51 | 17 of 31 | 1 | 2 | numerical | Compare pure ALOHA, slotted ALOHA, CSMA, CSMA/CD on start rule, vulnerable time and post-collision behaviour; state wireless suitability. (cite BCSE30 |
| 4 | Topologies / network types | M1 | 0.69 | 8 of 11 | 0.73 | 17 of 22 | 1 | 0 | scenario | Identify topology of each network, I/O ports per device, dedicated links needed, and failure consequences for 240 devices. (cite BCSE308L-CAT1-C2-2026 |
| 5 | Distance vector routing | M5 | 0.69 | 8 of 11 | 0.71 | 15 of 20 | 1 | 1 | theory | Show step-by-step distance vector operation for R1 with iteration table, shortest path tree for R1 and routing table entries. (cite BCSE308L-CAT-2-C2- |
| 6 | TCP congestion control | M6 | 0.69 | 8 of 11 | 0.69 | 8 of 11 | 0 | 1 | theory | Identify time intervals of TCP slow start from Figure 3 (cite BCSE308L-FAT-A1-2025-2026:Q8ia) |
| 7 | Link state / Dijkstra | M5 | 0.69 | 8 of 11 | 0.67 | 14 of 20 | 1 | 0 | trace | Write LSAs of A, C, F; explain identical domain picture; run Dijkstra from A with permanent/tentative lists; draw tree and routing table. (cite BCSE30 |
| 8 | Error detection (CRC/checksum/parity) | M3 | 0.69 | 8 of 11 | 0.54 | 17 of 31 | 2 | 2 | numerical | Compute checksum for seven 8-bit words with specified bit flips, form packets, verify, decide acceptance, explain one's complement arithmetic. (cite B |
| 9 | Delay / throughput calculation | M2 | 0.61 | 7 of 11 | 0.77 | 17 of 22 | 2 | 1 | numerical | Compute end-to-end delay per packet for circuit switching, packet switching and all switching types given links, rates and queuing delay. (cite BCSE30 |
| 10 | IP fragmentation | M4 | 0.61 | 7 of 11 | 0.67 | 13 of 20 | 2 | 1 | numerical | Decode 20-byte IPv4 header fields and analyse fragmentation for a link of MTU 576. (cite BCSE308L-CAT-2-C1-2026-2027-Question Paper:Q3B) |
| 11 | OSI vs TCP/IP layers | M1 | 0.54 | 6 of 11 | 0.65 | 14 of 22 | 2 | 1 | theory | Draw layered model for air-travel activities mapped to a communication layer, explain each layer, discuss layering advantages and disadvantages. (cite |
| 12 | DNS | M7 | 0.46 | 5 of 11 | 0.46 | 5 of 11 | 0 | 0 | theory | Name labels, hierarchy levels, FQDN/PQDN, domain type of ece.chennai.vit.ac.in and why DNS (cite BCSE308L-FAT-A1-2025-2026:Q9i) |
| 13 | Flow control (stop-and-wait/GBN/SR) | M3 | 0.46 | 5 of 11 | 0.41 | 12 of 31 | 2 | 1 | trace | Construct sender/receiver state flow diagram for Stop-and-Wait ARQ with 11 frames, every 4th lost, and count transmissions. (cite BCSE308L-CAT-2-C1-20 |
| 14 | IPv6 | M4 | 0.46 | 5 of 11 | 0.38 | 8 of 20 | 0 | 0 | theory | Check whether two IPv6 address notations are valid. (cite BCSE308L-FAT-F1-2025-2026:Q5ii) |
| 15 | Hamming code | M3 | 0.39 | 4 of 11 | 0.41 | 12 of 31 | 2 | 1 | numerical | Find redundancy bits for 16-bit data and build 11-bit even-parity Hamming codeword for K (1001011); then locate/correct error in 10011110110. (cite BC |
| 16 | HTTP | M7 | 0.39 | 4 of 11 | 0.39 | 4 of 11 | 0 | 1 | theory | Trace DNS, HTTP, SMTP, TCP, IP interaction for simultaneous web download and email and explain cross-layer cooperation. (cite BCSE308L-FAT-G2-2025-202 |
| 17 | Congestion control (open/closed loop) | M6 | 0.31 | 3 of 11 | 0.31 | 3 of 11 | 0 | 0 | theory | Explain congestion control techniques used to improve QoS. (cite BCSE308L - FAT - D1 - 2024 - Question Paper:Q7) |
| 18 | Network security basics | M7 | 0.31 | 3 of 11 | 0.31 | 3 of 11 | 0 | 2 | theory | Specify features of an IoT application-layer protocol (low bandwidth, scalability, security, latency) and compare with HTTP or MQTT. (cite BCSE308L-FA |
| 19 | FTP | M7 | 0.31 | 3 of 11 | 0.31 | 3 of 11 | 0 | 0 | theory | Describe the two FTP connections, transferable file types, and three transmission modes. (cite BCSE308L-FAT-F1-2025-2026:Q8i) |
| 20 | SMTP / POP / IMAP | M7 | 0.31 | 3 of 11 | 0.31 | 3 of 11 | 0 | 1 | theory | Illustrate with diagram SMTP over TCP transfer of Alice's email to Bob's mailbox (cite BCSE308L-FAT-F2-2025-2026:Q7ii) |
| 21 | TCP header / handshake | M6 | 0.23 | 2 of 11 | 0.23 | 2 of 11 | 0 | 2 | numerical | Decode TCP header hex dump: source port, seq, ack, header length, segment type, window. (cite BCSE308L-FAT-F1-2025-2026:Q7i) |
| 22 | Application & transport protocols | M7 | 0.23 | 2 of 11 | 0.23 | 2 of 11 | 0 | 0 | theory | Identify four application and transport protocols with their purposes. (cite BCSE308L - FAT - D1 - 2023 - Answer Key:Q1b) |

Teach order (I): tier p >= 0.75 by module, then 0.50-0.75, then the rest (`teach_order`).

## 4. Drift: 2026-27 vs older (O; small n)

| exam | group | papers | mean Bloom | scenario wrapper % q | theory % marks | (num+trace):theory |
|---|---|---|---|---|---|---|
| CAT1 | older | 9 | 3.15 | 42.4 | 40.8 | 1.28 |
| CAT1 | recent_2026_27 | 2 | 3.14 | 64.3 | 0.0 | None |
| CAT2 | older | 7 | 2.94 | 25.3 | 16.2 | 5.15 |
| CAT2 | recent_2026_27 | 2 | 3.64 | 78.6 | 5.0 | 19.0 |
| FAT | older | 11 | 3.13 | 34.8 | 38.6 | 1.21 |
| all | scenario wrapper % by start year | 2022: 35.0, 2023: 35.7, 2024: 28.6, 2025: 37.8, 2026: 71.4 | | | | |

2026-27 CATs (C1, C2) carry more scenario-wrapped questions: CAT-1 64% vs 43% older, CAT-2 79% vs 28% older (O, 2 papers each; CN wrapper tags 9/13 accurate). Bloom flat for CAT-1 (3.14 vs 3.16), higher for CAT-2 (3.64 vs 2.97).

## 5. Slot pairs and sister courses (I: rule-based matching)

| comparison | n q | Identical | Same concept new numbers | Same module only | Unrelated |
|---|---|---|---|---|---|
| slot 1 -> slot 2, same exam+year (9 pairs) | 132 | 0.0 | 0.735 | 0.258 | 0.008 |
| different letter, same year (17 pairs) | 239 | 0.0 | 0.649 | 0.31 | 0.042 |
| baseline: same exam, different year (240 pairs) | 3309 | 0.002 | 0.647 | 0.328 | 0.023 |
| sister course vs core, same exam+year (35 pairs) | 324 | 0.0 | 0.586 | 0.383 | 0.031 |

Slot 1 -> slot 2 shares the archetype for 0.735 of questions vs 0.647 between different years: a modest lift (O). FAT F1 -> F2 2025-26: 15 of 25 same archetype. Whole CAT papers were shared across slot letters twice in 2023-24 (B1 = D1 CAT-1; D1 = F1 CAT-2), so same-session slots can receive the same paper.

## 6. Answer keys: what earns marks (O)

91 key rows; step marks stated in 18; penalties stated in 0.

| topic | mandatory elements from real keys |
|---|---|
| IPv4 addressing / subnetting / CIDR | key shows: 50 to /26 (.0-.63); 25 to /27 (.64-.95); 12 to /28 (.96-.111) [BCSE308L-CAT2-F1-2025-2026-AK:Q2]<br>key shows: class from first octet; default masks [BCSE308L-CAT2-F1-2025-2026-AK:Q3b] |
| Circuit vs packet switching | key shows: each user needs 1 Mbps [BCSE308L-CAT1-F1-2025-2026-AK:Q3i]<br>key shows: two users need 2 Mbps (no queue); three users need 3 Mbps above 2 Mbps link [BCSE308L-CAT1-F1-2025-2026-AK:Q3ii] |
| MAC (ALOHA/CSMA/CD/CA) | key shows: Tf=1 ms; slots per second 1000; S=G e^-G [BCSE308L-CAT2-F1-2025-2026-AK:Q1a]<br>key shows: collision detection not feasible in wireless; hidden-node problem; RTS/CTS; ACK [BCSE308L-CAT2-F2-2025-2026-AK:Q1B] |
| Topologies / network types | key shows: Library 10x15; Science 12x18; Administration 8x12 [BCSE308L-CAT1-F2-2025-2026-AK:Q1a]<br>key shows: single ring 40+35+45=120 m; dual ring 2x120 [BCSE308L-CAT1-F2-2025-2026-AK:Q1b] |
| Distance vector routing | key shows: Bellman-Ford steps; n-1 = 5; next-hop tables [BCSE308L-CAT2-F1-2025-2026-AK:Q5]<br>key shows: d_x(y) = min over neighbours {c(x,v)+d_v(y)} [BCSE308L-CAT2-F2-2025-2026-AK:Q5] |
| Link state / Dijkstra | key shows: F-E 1; F-B 4; E-D 4; D-C 1 [BCSE308L-CAT2-F1-2025-2026-AK:Q4]<br>key shows: A-C 1; A-C-D 3; A-C-D-E 4; A-C-D-B 6 [BCSE308L-CAT2-F2-2025-2026-AK:Q4] |
| Error detection (CRC/checksum/parity) | key shows: divisor 1001; remainder 011; codeword 11001001011; non-zero remainder at receiver [BCSE308L-CAT1-F1-2025-2026-AK:Q4]<br>marks: VRC 2.5; LRC 2.5; CRC 2.5; Checksum 2.5 [BCSE308L-CAT1-F2-2025-2026-AK:Q4a] |
| Delay / throughput calculation | key shows: store-and-forward; L/R1; L/R2 [BCSE308L-CAT1-F1-2025-2026-AK:Q2a]<br>key shows: bottleneck link; 4x10^6x8 bits; 500 kbps; 100 Kbps [BCSE308L-CAT1-F1-2025-2026-AK:Q2b] |
| IP fragmentation | key shows: IHL=7; TTL 0x20; protocol 0x06; DF=1; ID 3 [BCSE308L-CAT2-F2-2025-2026-AK:Q3]<br>key shows: not fragmented (offset 0, flag 0); data = 84-20 = 64 bytes; TTL 0x20 so 32 more routers; identification 0003; offset 0; source 124.78.3.2; destination 180.14.15 [BCSE308L-CAT-2-D1-2023-2024-Answer Key:Q3b] |
| OSI vs TCP/IP layers | key shows: fault tolerance-network layer; speed matching-link and transport; data integrity-link and transport (CRC/checksum); segmentation-transport; node-MAC; host-IP; p [BCSE308L-CAT1-F1-2025-2026-AK:Q1a]<br>key shows: NL-1, DL-1, PL-1 per intermediate router [BCSE308L-CAT1-F1-2025-2026-AK:Q1b] |
| DNS | marks: iterative 5; key shows: iterative query; referral; diagram [BCSE308L - FAT - D1 - 2023 - Answer Key:Q8a]<br>marks: recursive 5; key shows: recursive query; delegation to servers; diagram [BCSE308L - FAT - D1 - 2023 - Answer Key:Q8b] |
| Flow control (stop-and-wait/GBN/SR) | key shows: Td=4.096 ms; Tp=22.5 ms; eta=Td/(Td+2Tp) [BCSE308L-CAT2-F1-2025-2026-AK:Q1b]<br>key shows: WS=8; range 0-511; expected 100 [BCSE308L-CAT2-F2-2025-2026-AK:Q1Aa] |
| IPv6 | key shows: address space 32 vs 128 bit; auto-configuration; fixed 40-byte header; IPsec optional vs built-in; no broadcast [BCSE308L-CAT2-F1-2025-2026-AK:Q3a]<br>key shows: any six of: 32-bit vs 128-bit address; dotted decimal vs hexadecimal; IPv6 has no classes; no VLSM in IPv6; fragmentation by senders only in IPv6; no checksum i [BCSE308L-CAT-2-D1-2023-2024-Answer Key:Q3a] |
| Hamming code | key shows: check bits C1 C2 C4 C8; syndrome [BCSE308L-CAT1-F1-2025-2026-AK:Q5a]<br>key shows: 8-bit data words; column by column transmission [BCSE308L-CAT1-F1-2025-2026-AK:Q5b] |
| Congestion control (open/closed loop) | marks: closed loop 5; key shows: two closed-loop mechanisms [BCSE308L - FAT - D1 - 2023 - Answer Key:Q9a]<br>marks: open loop 5; key shows: two open-loop mechanisms [BCSE308L - FAT - D1 - 2023 - Answer Key:Q9b] |
| Network security basics | marks: any 5 measures, 2 marks each; key shows: any five IoT cloud security measures [BCSE308L - FAT - D1 - 2023 - Answer Key:Q10] |
| Application & transport protocols | marks: TCP,UDP 2; FTP,SMTP 2; key shows: TCP; UDP; FTP; SMTP [BCSE308L - FAT - D1 - 2023 - Answer Key:Q1b] |
| NAT / DHCP / ARP / ICMP | key shows: PAT; private ports 50000-50002; public ports 40001-40003 [BCSE308L-CAT2-F2-2025-2026-AK:Q2B]<br>key shows: Network Address Translation (NAT); key gives only the name, explanation marked 'to be explained' [BCSE308L-CAT-2-D2-2024-2025-Answer Key:Q3b] |
| Bluetooth / short-range wireless | key shows: Bluetooth [BCSE308L - FAT - D1 - 2023 - Answer Key:Q4b] |
| Sliding window efficiency | key shows: GBN timing diagram; every 5th frame lost; timeout retransmission of window; 18 frames sent in total; efficiency 10/18 [BCSE308L-CAT-2-D1-2023-2024-Answer Key:Q1a(i)]<br>key shows: SR timing diagram; every 5th frame lost; only lost frames retransmitted; 12 frames sent in total; efficiency 10/12 [BCSE308L-CAT-2-D1-2023-2024-Answer Key:Q1a(ii)] |
| Wireless LAN (802.11) BSS/ESS | marks: 1 mark IEEE 802.11; 4 marks architecture; key shows: IEEE 802.11 wireless LAN; basic service set (BSS); access point (AP); distribution system (DS); extended service set (ESS); portal to IEEE 802.x LAN; same MAC p [BCSE308L-CAT-2-D2-2024-2025-Answer Key:Q1b] |

## 7. Observed traps

- IPv4 addressing / subnetting / CIDR: Allocate largest blocks first (50 hosts -> /26, 25 -> /27, 12 -> /28) and give exact ranges [BCSE308L-CAT2-F1-2025-2026-AK:Q2]
- IPv4 addressing / subnetting / CIDR: After allocating all branches, also asked for the number of addresses left [BCSE308L-FAT-F2-2025-2026:Q4]
- MAC (ALOHA/CSMA/CD/CA): Collision detection is not feasible in wireless (hidden node), so CSMA/CA with RTS/CTS and ACK [BCSE308L-CAT2-F2-2025-2026-AK:Q1B]
- Delay / throughput calculation: Circuit-switched delay = setup/teardown bits + data bits over rate + propagation; compute for 3 data sizes then conclude on efficiency [BCSE308L-FAT-F2-2025-2026:Q2]
- IP fragmentation: Different MTU per link: fragment at R1 and again at R2, then count fragments arriving at Host B; offsets in 8-byte units [BCSE308L-FAT-F2-2025-2026:Q3iv]
- IP fragmentation: Header given in hex: decode IHL, TTL, protocol, DF/MF and offset before answering [BCSE308L-CAT2-F2-2025-2026-AK:Q3]
- Leaky / token bucket: Token bucket maximum burst equals bucket capacity (hint printed) [BCSE308L-FAT-F2-2025-2026:Q6iv]

## 8. No clear pattern

- Exact question numbering of modules (F1/F2 2025-26 placed M3 last)
- Application-layer protocol choice: DNS 5/11, HTTP 4/11, SMTP 3/11, FTP 3/11
- Step-mark splits: rarely stated
- 2026-27 FAT style (no 2026-27 BCSE308L FAT)

Misfiled file excluded: `CN/PYQ/FAT/BCSE308L - FAT - B1 - 2024 - Question Paper (2).pdf` is an Optical Fiber Communications (BECE308L) paper.
