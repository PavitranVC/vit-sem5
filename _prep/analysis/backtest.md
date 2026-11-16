# Backtest: OS and AWS (completed exams)

Method (O for counts, I for design): for each 2026-27 slot-2 FAT, rank topics with the same formula used for AI, trained only on pre-2026-27 papers + 2026-27 CATs + the same-letter 2026-27 slot-1 FAT. Take the top 10 and count how many topics appear in the slot-2 FAT. Comparator: the 10 most frequent topics in pre-2026-27 FATs only.

| subject | target | slot-1 used | hits (precision) | recall of target topics | naive baseline hits | target topics also in slot-1 FAT |
|---|---|---|---|---|---|---|
| OS | BCSE303L-FAT-A2-2026-2027 | BCSE303L-FAT-A1-2026-2027 | 6 of 10 | 6 of 15 distinct target topics | 7 of 10 | 8 of 15 target topics also in slot-1 FAT |
| OS | BCSE303L-FAT-B2-Fall-2026-27 | BCSE303L-FAT-B1-2026-2027 | 6 of 10 | 6 of 16 distinct target topics | 5 of 10 | 5 of 16 target topics also in slot-1 FAT |
| AWS | BCSE355L-FAT-A2-Fall-2026-2027 | BCSE355L-FAT-A1-2026-2027 | 7 of 10 | 7 of 12 distinct target topics | 7 of 10 | 8 of 12 target topics also in slot-1 FAT |
| AWS | BCSE355L-FAT-B2-2026-2027 | BCSE355L-FAT-B1-2026-2027 | 3 of 10 | 3 of 11 distinct target topics | 3 of 10 | 2 of 11 target topics also in slot-1 FAT |

Pooled: **22 of 40 = 0.55 -> tier Medium** (High >= 0.70, Medium 0.50-0.69, Low < 0.50). Naive baseline pooled: 22 of 40.

Reading (O): the formula does no better than plain topic frequency in older FATs. A topic-level prediction gets about half to two-thirds of a FAT's top topics right. A slot-1 FAT shared 8 of 12 topics with its slot-2 pair in AWS A, but only 2 of 11 in AWS B: slot pairing is not reliable.
Small n: 4 target papers, 40 predictions. The tier is a rough guide, not a calibrated confidence.

Missed topics (what a top-10 list would not have covered):
- OS BCSE303L-FAT-A2-2026-2027: Deadlock conditions/prevention; Deadlock detection / RAG; Directory structure; Protection / access matrix; Security threats; Segmentation; TLB / EAT; Threads / multithreading; Virtual machines / hypervisor
- OS BCSE303L-FAT-B2-Fall-2026-27: Demand paging; Dining philosophers; Directory structure; Disk structure / addressing; Distributed file systems; Dual-mode operation; Paging / address translation; Protection / access matrix; TLB / EAT; Thrashing / working set
- AWS BCSE355L-FAT-A2-Fall-2026-2027: Global infrastructure / multi-region DR; Route 53 routing policies; Server migration / 6 Rs; Step Functions / SWF; Well-Architected pillars
- AWS BCSE355L-FAT-B2-2026-2027: Aurora; CloudFront; DMS; DynamoDB; EC2 instance types / launch / pricing; KMS / encryption; Server migration / 6 Rs; Step Functions / SWF

This tier is written to `backtest_confidence` in every patterns.json.
