# CAD (AWS Solutions Architect) FAT analysis

Built from the 5 FAT papers in `_prep/pyq-index/CAD.md` (A1, A2, G1, G2 Nov 2025; F1 Nov 2024), with CAT-2 papers used as a second signal. Every FAT is 10 questions x 10 marks. Some index entries were read from photos or garbled text, so treat counts as accurate to about +/-1.

## 1. Module weightage (teacher's note vs what the papers show)
Teacher's note (from the student): M1, M2, M4, M6 = 10 marks each; M3, M5, M7, M8 = 20 marks each. That sums to 120, not 100, so read it as a guide to which modules get a choice or a second part, not as exact marks.

| Module | Questions in 5 FATs | Papers with an either/or in this module |
|---|---|---|
| M1 Foundations, shared responsibility, IAM | 7 | 0 |
| M2 Compute + storage | 7 | 0 |
| M3 Networking | 6 | 1 (G2) |
| M4 Databases | 6 | 0 |
| M5 Monitoring, audit, cost | 7 | 2 (A1, A2) |
| M6 Security | 5 | 1 (G2) |
| M7 Integration + Well-Architected | 7 | 2 (G1, F1) |
| M8 Migration | 5 | 4 (A1, A2, G1, F1) |

Every paper has exactly 2 either/or questions, so 10 of the 50 questions offer a choice.

The either/or questions fall in M8 (4 of 5 papers), M5, M7, M3 and M6. M1, M2 and M4 never have a choice, so the 10-mark modules in the teacher's note (M1, M2, M4) are the ones where you must answer what is asked. M6 is the exception: it got an either/or once.

### Either/or pairs seen (you answer only one)
- M8: Snow family vs DMS/SMS. Seen as: A1 DMS (Oracle to Aurora) vs Snowball Edge 50 TB; A2 SMS vs Snowball/Snowball Edge/Snowmobile comparison; G1 Snow Family recommendation vs SMS+DMS hybrid; F1 SMS vs Snowball Edge. Snow family is on one side of the choice every time.
- M5: A1 CloudWatch+CloudTrail+SNS (detect misuse) vs Config+Systems Manager+Lambda (compliance); A2 detect/respond to rising costs and unauthorized calls vs Free Tier overrun (Budgets, Trusted Advisor).
- M7: G1 SNS alerting vs Step Functions claims workflow; F1 SQS order flow vs Step Functions orchestration.
- M3 (G2): two-VPC routing and traffic rules vs on-prem to VPC connectivity (Site-to-Site VPN).
- M6 (G2): WAF design vs comparing the four encryption options (client-side / server-side).

## 2. Question position pattern
In G1 and G2 the questions run in module order: Q1-2 M1, Q3-4 M2, Q5 M3, Q6 M4, Q7 M5, Q8 M6, Q9 M7, Q10 M8. A1/A2 run similarly but with extra M5/M7/M4 questions at Q9/Q10. F1 (2024) is the same order with two M3 and two M5 questions. So expect a question from every module in every paper.

## 3. Topics by how often they appeared (FAT, 5 papers)
### Appeared in every paper (must know cold)
- VPC design: public + private subnet, IGW, NAT gateway, route tables, security groups, NACLs, with a diagram (A1 Q3, A2 Q3, G1 Q5, G2 Q5, F1 Q1 and Q4). Also CAT-2 F1 Q1, F2 Q1.
- A database design question: RDS Multi-AZ + Read Replicas, Aurora, DynamoDB vs RDS (A1 Q4, A2 Q4+Q9, G1 Q6, G2 Q6, F1 Q5). Multi-AZ + Read Replicas is in 4 of 5 papers and in most CAT-2 papers.
- An M6 security question: Shield (G1, F1, plus A2), WAF (A1, A2, G2), KMS/encryption (A1, A2, G2).
- M8 migration: Snow family and DMS/SMS (one question in all 5 papers).

### 4 of 5 papers
- IAM: users, groups, roles, policies, least privilege, writing a policy (A2, G1, G2, F1).
- CloudWatch + CloudTrail + Config together (A1, A2, G1, plus CloudWatch recovery in F1).
- Step Functions (and SQS/SNS/SWF around it) in A2, G1, G2, F1.

### 3 of 5 papers
- Auto Scaling + ELB for variable load (A1, A2, G2).
- Choosing storage (S3 / EFS / EBS / Glacier, lifecycle policies) (A2, G1, F1).
- Cost control: Budgets, Cost Explorer, Trusted Advisor (A1, A2, F1). Also CAT-2 A1 Q4, A2 Q4, F1 Q5, F2 Q5.

### 2 of 5 papers
- Shared responsibility model (A1, G1). CAT-2 A1 Q5 too.
- Well-Architected pillars (A1 x2, A2).
- EC2 launch steps / lifecycle (G1, G2).
- Systems Manager + Config remediation (A1, G2).
- Security group vs NACL (G1, F1). CAT-2 G2 asks for NACL rule tables.

### Once so far (easy marks if you know them)
- NIST: 5 characteristics, 3 service models, 4 deployment models (G2 Q1).
- AWS Global Infrastructure: Regions, AZs, edge locations (G1 Q1).
- Write an IAM policy JSON (G2 Q2).
- SWF vs Step Functions comparison (G2 Q9).
- Site-to-Site VPN / Direct Connect, VPC peering, CloudFront (G2 Q5b, A2 Q3; CAT-2 F1 Q2, F2 Q2, G1 Q1).
- VPC CIDR planning: four /24 subnets, 251 usable addresses each (CAT-2 F2 Q1).

## 4. Priority order for revision
1. VPC diagram and SG vs NACL (M3)
2. RDS Multi-AZ vs Read Replica, Aurora, DynamoDB choice (M4)
3. IAM + shared responsibility (M1)
4. Auto Scaling + ELB, storage selection (M2)
5. CloudWatch / CloudTrail / Config split, then Budgets / Trusted Advisor (M5)
6. Shield, WAF, KMS and the encryption types (M6)
7. Snow family, then DMS/SMS (M8)
8. Step Functions, SQS, SNS, Well-Architected pillars (M7)
9. One-offs: NIST, Global Infrastructure, IAM policy JSON, VPN/Direct Connect, CloudFront

## 5. What to skip if time runs out
- SWF details beyond the comparison with Step Functions.
- Systems Manager sub-tools beyond inventory, patching and automation.
- Pricing slides, KMS key-policy detail, Snowmobile detail beyond capacity.
- Knowledge Check and lab slides.
