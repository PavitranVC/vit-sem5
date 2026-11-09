# CAD study guide: blocks for 7-8 Nov (first pass), then revision

Files are in the `AWS/` folder. Page numbers come from `_prep/study-guide/CAD-slide-map.md` (full page-by-page titles).
Goal of the first pass: understand the structure of each service and build the one-page comparison tables below. Don't try to memorise yet. Memory comes from the revision blocks (9, 11, 12 Nov) when you recall from the tables and answer PYQ scenarios.

## How CAD FAT questions are shaped (from the 5 FAT papers in the repo)
Every paper is 10 questions x 10 marks, each a business scenario ("A company wants X; design/explain with AWS services"). Your answer is a structured design, not a definition. Use this template for every scenario answer, and practise it in revision:
1. Requirement: restate the 2-3 problems in the scenario in one line each
2. Services: name the exact AWS services chosen
3. How they connect: a small diagram (boxes and arrows)
4. Why: one line per requirement (availability, scalability, security, cost)
Because the structure is the same every time, you only need to learn the services; the layout of the answer is automatic.

Note: the four first-pass blocks are split by slide load, so they differ slightly from the module labels in the schedule table (M2 storage sits in block 2, M4 in block 3, M6-M8 in block 4). If you run over, push the Module 6 detail slides (KMS, WAF, Shield) into the Mon 9 Nov revision block. Finishing the tables matters more than reading every page.

## Block 1: Sat 7 Nov, morning (M1 + M2 compute)
Learn:
- `Module 1/M1_Session1.pdf` pp.2-5 (NIST characteristics), 9-11 (service and deployment models), 19, 22-28 (Regions, Availability Zones, data centers, Points of Presence). Skip the Knowledge Check slides.
- `Module 1/M1_Session2.pdf` pp.2-8 (shared responsibility), 9-22 (IAM: users, groups, roles, policies, MFA, best practices). Skip the lab slide.
- `Module 2.pdf` pp.2-37 (compute options, EC2 launch steps, instance types, lifecycle, ELB), pp.38-49 (Auto Scaling), pp.50-59 (pricing models + the four cost pillars).
Build as you go (on paper or in notes):
- Table 1: EC2 pricing models (On-Demand, Reserved, Spot, Savings Plans, Dedicated) vs when to use
- Table 2: Shared responsibility: AWS (security OF the cloud) vs customer (security IN the cloud)
- The 9 EC2 launch steps in order (appeared as an exam question)

## Block 2: Sat 7 Nov, afternoon (M2 storage + M3 networking)
Learn:
- `Module 2.pdf` pp.61-99 (EBS, S3 and storage classes, EFS, Glacier, lifecycle policies, comparison, encryption). Skip pricing slides pp.80-82 on the first pass.
- `Module 3.pdf` pp.9-18 (VPC, subnets, reserved IPs, route tables, IGW, NAT), pp.21-31 (peering, Site-to-Site VPN, Direct Connect, endpoints, transit gateway), pp.32-39 (security groups vs NACLs), pp.43-58 (Route 53, CloudFront).
Build:
- Table 3: EBS vs S3 vs EFS vs Glacier (type, use case)
- Table 4: S3 storage classes + lifecycle policy idea
- Table 5: Security group vs NACL (stateful/stateless, level, rules)
- Table 6: VPC connectivity: peering vs Site-to-Site VPN vs Direct Connect vs transit gateway
- One standard diagram: VPC with public subnet (IGW) + private subnet (NAT) + route tables + SG/NACL. It's needed in almost every networking question.

## Block 3: Sun 8 Nov, morning (M4 databases + M5 monitoring and cost)
Learn:
- `Module4.pdf` pp.4-34 (RDS, Multi-AZ, read replicas, Aurora, RDS vs Aurora), pp.35-57 (DynamoDB core concepts, keys, partitioning, indexes, Streams). Pages 58-72 repeat Streams; skim.
- `Module 5/AWS CloudWatch.pdf` pp.3-14, `Module 5/CloudTrial.pdf` pp.2-11 and 14-15 (CloudWatch vs CloudTrail), `Module 5/Module-5.pdf` pp.3-35 (Config, Systems Manager and other management tools), `Module 5/AWS Cost Management.pdf` pp.7-19 (Budgets, Free Tier, Trusted Advisor).
Build:
- Table 7: RDS vs Aurora vs DynamoDB (when to choose each)
- Table 8: Multi-AZ (availability, standby) vs Read Replica (read scaling)
- Table 9: CloudWatch (metrics/alarms) vs CloudTrail (API audit log) vs Config (config compliance) vs Systems Manager
- Table 10: Cost tools: Billing, Cost Explorer, Budgets, Trusted Advisor, Free Tier

## Block 4: Sun 8 Nov, afternoon (M6 security + M7 integration + M8 migration)
Learn:
- Module 6 files: `AWS KMS.pdf`, `WAF.pdf`, `AWS Shield.pdf`, `Shared Responsibility model.pdf`, `Security best Practices.pdf` (skim the first 3 for what each protects against)
- `Dhivyaa CR's AWS Notes[external]/..._Module-7.pdf`: pp.6-25 (SQS), 26-44 (SNS), 45-63 (SWF), 64-81 (Step Functions), 82-101 (Well-Architected, scalability, HA and fault tolerance)
- `Dhivyaa CR's AWS Notes[external]/..._Module-8.pdf`: pp.15-34 (DMS, SMS), 35-51 (Snow Family and comparison)
UPDATE 9 Nov: your teacher's own Module 7 and 8 files are now in the repo (`AWS/Module 7/` and `AWS/BCSE355L_Module-8.pdf`). Use those first; page map is at the end of `CAD-slide-map.md`. The external notes are the backup for Standard vs Express workflows and the Schema Conversion Tool.
Build:
- Table 11: KMS vs WAF vs Shield (what each stops)
- Table 12: SQS vs SNS vs SWF vs Step Functions
- Table 13: Snowball vs Snowball Edge vs Snowmobile (capacity, use) + DMS vs SMS
- The 6 Well-Architected pillars with one line each

## Revision blocks
- Mon 9 Nov morning (revision 1): recall tables 1-13 from a blank page, then check against the slides.
- Wed 11 Nov morning (revision 2): answer PYQ scenarios from `_prep/pyq-index/CAD.md` using the 4-line template; open the actual paper PDFs from `AWS/PYQ/FAT` and `AWS/PYQ/CAT2`.
- Thu 12 Nov morning (final recall): tables again, from memory, then fix the gaps.
- Thu 12 Nov afternoon: timed scenario practice (about 10 questions, 15 minutes each, using the 4-line template).


## Update 9 Nov: Module 7 and 8 from the teacher's files
Modules 7 and 8 carry 20 marks each in the FAT, and the teacher's CAT-2 DA lists 8 questions, all from these two modules. Treat that list as the likely FAT questions. Work through them in this order:
- Mon 9 Eve (about 90 min from 21:00): DA Q1 to Q4. SQS (`Module 7/BCSE355L_SQS.pdf`), SNS (`BCSE355L_SNS.pdf`), fan-out (SQS pp.18-19), SWF and Step Functions (`BCSE355L_Module-7.pdf` pp.2-19). End with the SQS vs SNS and SWF vs Step Functions tables from memory. For Q4, read external Module 7 pp.66-68.
- Tue 10 AM: DA Q5 to Q8. Six pillars (`BCSE355L_Module-7.pdf` pp.20-29), then `BCSE355L_Module-8.pdf`: Server Migration and Transform MGN (pp.7-11), DMS (pp.12-19), Snow family (pp.20-33), and the hybrid services page list (pp.4-6).
For each DA question write the answer once in the 4-line template, 10 minutes each. That is your answer bank.
