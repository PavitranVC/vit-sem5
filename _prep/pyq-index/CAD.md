# CAD (BCSE355L Cloud Architecture Design / "AWS Solutions Architect"): raw question index (NO analysis yet)

Source files: `AWS/PYQ/FAT/` and `AWS/PYQ/CAT2/`. Module key (syllabus): M1 Cloud/AWS foundations, shared responsibility, IAM | M2 Compute (EC2, ELB, Auto Scaling) and Storage (EBS, S3, EFS, Glacier) | M3 Networking (VPC, subnets, routes, SG, peering, Direct Connect, CloudFront) | M4 Databases (RDS, Multi-AZ, read replicas, Aurora, DynamoDB, Streams) | M5 Management + cost (CloudWatch, CloudTrail, Config, Systems Manager, Budgets, Trusted Advisor, Free Tier) | M6 Security (KMS, WAF, Shield, best practices) | M7 App integration (SQS, SNS, SWF, Step Functions) + Well-Architected, HA/fault tolerance, scalability | M8 Migration (DMS, SMS, Snowball family)

Format of every FAT paper below: 3 hrs, 10 x 10 marks, scenario/design questions (a few have an OR choice). CAT-2 papers: 90 min, 50 marks, 5 scenario questions x 10.
Some papers are phone photos (G1, G2 FAT); text was read from the images.

## FAT Nov 2025, A1+TA1
1. M1/M6 FinTech moves payment system to AWS: how Shared Responsibility Model shapes security design; AWS vs customer tasks
2. M2 unpredictable traffic spikes: auto-adjust compute, distribute requests evenly, avoid overprovisioning, cost efficiency (Auto Scaling + ELB)
3. M3 multi-tier app across public/private subnets: VPC with route tables, NAT gateway, security groups; isolation + controlled internet access
4. M4 data analytics startup choosing RDS vs DynamoDB for transactional vs analytical workloads (question text partly garbled)
5a. M5 healthcare platform: detect unauthorized access/misuse with CloudWatch, CloudTrail, SNS (auditing + alerting) / 5b. M5 gov cloud: continuous configuration compliance + auto-remediation with Config, Systems Manager, Lambda
6. M6 audit found unencrypted data + traffic bursts on web apps: layered security design (data protection, identity, threat prevention)
7. M7 retail enterprise high costs: Well-Architected Cost Optimization pillar, misconfigurations, 3 recommendations with justification
8a. M8 Oracle on-prem -> Aurora with DMS: steps, minimal downtime, data consistency / 8b. M8 50 TB archived video from remote offline site via Snowball Edge: transfer, encryption, import stages
9. M5 team exceeds monthly budget: financial control plan: real-time tracking, proactive alerts, optimization recommendations (Budgets, Cost Explorer, Trusted Advisor)
10. M7 [BL6] design highly available, fault-tolerant, secure multi-tier e-commerce architecture: name exact services (compute, networking, DB, storage, monitoring, security) and justify vs best practices

## FAT Nov 2025, A2+TA2
1. M1 HealthSync: how IAM gives secure access control; two IAM features that enhance security
2. M2 Streamify video encoding + storage with fluctuating traffic: compute services/features for variable load; storage services + policies for cost optimization
3. M3 secure HA multi-region web app: public web tier, private app + DB tiers, global content delivery: complete network architecture
4. M4 global ride-sharing: Aurora PostgreSQL (relational) + DynamoDB (location/session): HA, fault tolerance, scalability, cost optimization design
5a. M5 rising costs + misconfigured resources + unauthorized API calls: services to detect/respond, monitor performance / 5b. M5 dev/test Free Tier overrun: how Budgets alerts, how Trusted Advisor optimizes
6. M6 financial services PCI-DSS/GDPR: public S3 buckets, SQL injection + XSS, no key management: WAF + Shield for SQLi/XSS/DDoS; KMS for keys across S3 and RDS
7. M7 compliance + HA + dynamic scaling app with degradation, cost spikes, audit failure: Well-Architected re-design using at least 3 pillars
8a. M8 migrate DBs with minimal downtime + lift-and-shift app servers, secure connectivity: how SMS migrates on-prem Windows servers / 8b. M8 10 PB archived video, limited bandwidth: compare Snowball vs Snowball Edge vs Snowmobile (capacity, use cases)
9. M4 RDS PostgreSQL Multi-AZ but slow reads at peak: architecture with Multi-AZ + Read Replicas (availability, performance, compliance)
10. M7 [BL6] serverless bookstore order fulfillment: SQS decoupling, SNS notifications (email/SMS), Step Functions orchestrating payment/inventory/shipping

## FAT Nov 2025, G1+TG1 (photo)
1. M1 global e-commerce start-up: how AWS Global Infrastructure gives low latency/HA; responsibilities of AWS vs customer
2. M1 least privilege: IAM users, roles, policies, groups for role-specific access and separation of duties
3. M2 [BL1] EC2: instance families, use cases, complete instance lifecycle (launch to termination)
4. M2 WebStream CMS single web server + attached storage: recommend AWS storage (EFS/S3 type) with key features, resilience, scalability, automated data management
5. M3 secure scalable VPC: public + private subnets, IGW, NAT gateway, route tables, security groups, NACLs; architecture diagram; isolation, controlled access, HA
6. M4 legacy e-commerce DB -> AWS relational DB: HA + read scalability architecture (Multi-AZ + read replicas / Aurora)
7. M5 suspected breach: CloudTrail + CloudWatch + Config together for investigation, root cause, resolution
8. M6 media streaming DDoS during live event: how AWS Shield protects
9a. M7 logistics real-time alerting: SNS design (multi-channel, reliable delivery, access controls) / 9b. M7 insurance claims workflow: sequential + parallel tasks, retries, fault tolerance (Step Functions)
10a. M8 8 PB sensor data from global factories: recommend Snow Family service, compare with others / 10b. M8 university data center -> AWS hybrid: strategy with SMS (servers) + DMS (structured data), minimal downtime

## FAT Nov 2025, G2+TG2 (photo)
1. M1 [BL1] NIST definition: 5 essential characteristics, 3 service models, 4 deployment models with examples; AWS vs on-prem similarities; diagram
2. M1 [BL6] essential elements of an IAM policy + write one policy: allow all on all DynamoDB tables except "Table1", allow all on all S3 objects except "Object1.txt"
3. M2 web tier internet-reachable, DB private, auto failover across AZs: how Auto Scaling handles overload/failover step by step, with diagram
4. M2 nine-step process to launch an EC2 instance, with options and decision choices at each step
5a. M3 ShopGlobal two VPCs (Web-VPC 10.0.0.0/16, Payment-VPC 10.0.0.0/16 variants given): subnets, route tables; traffic rules (web can initiate to payment, payment cannot initiate to web, no internet to payment) / 5b. M3 on-prem corporate datacentre 192.168.10.0/24 <-> VPC 10.0.0.0/16, low cost, fast setup, encrypted over internet: choose connectivity (Site-to-Site VPN), diagram, route tables
6. M4 GlobalStream PostgreSQL on RDS: peak read spike + 5-min outage during AZ maintenance: RDS feature combination (read replicas + Multi-AZ), cost-effective
7. M5 fintech 250 Linux EC2s across 2 accounts, 2 regions, private subnets: integrate Systems Manager for inventory/config tracking, automated remediation with approval, change control, 24x7 incident response; diagram
8a. M6 healthcare app behind ALB, SQLi + XSS + DDoS + IP blacklist: WAF-based design with sample rules, avoid false positives / 8b. M6 compare Client-Side Encryption (Client), CSE (S3), Server-Side Encryption (Client), SSE (S3) with diagrams
9. M7 [BL5] compare and contrast SWF vs Step Functions
10. M8 500 GB on-prem MySQL -> RDS PostgreSQL, 15-min max downtime, incompatible types/stored procedures: DMS strategy, schema conversion (SCT), consistency

## FAT Nov 2024, F1+TF1 ("AWS Solutions Architect")
1. M3 XYZ org moving workload: network configuration, resource provisioning, infrastructure design, combined architecture to distribute/administer data in AWS
2. M1 IAM admin accounts vulnerable: steps to lock them down; explain IAM policy and its role in access control
3. M2 multi-account, multi-region org needs centralized storage: suitable AWS storage services with key features and working (sharing data between instances, content management, big data analytics) [5]
4. M3 (i) configure VPC with subnets and necessary steps [5]; (ii) security groups and NACLs in VPC [5]
5. M4 large client-records DB with downtime and performance bottlenecks: identify AWS database service; design with multi-AZ for HA and read scalability
6. M5 manufacturing company unexpected AWS billing spike, underutilized resources + services in irrelevant regions: cost optimization steps/tools, easy identification of unwanted services/instances
7. M5 EC2 instance recovery steps with neat sketch (monitoring, CloudWatch recovery)
8. M6 AWS Shield: working against DDoS, with example
9a. M7 design order-flow system with SQS: key features for message durability and availability / 9b. M7 serverless orchestration service (Step Functions): create/manage multi-step workflows; states, activities, tasks
10a. M8 migration tool to move on-prem servers (SMS): key features and pros / 10b. M8 media company documentaries, spotty internet, terabytes/day local processing then upload: Snowball Edge requirements and secure transport

## CAT-2 papers (90 min, 50 marks)
### Fall 2025-26, A1+TA1 (5 x 10)
1. M4 e-commerce order DB: slow under surges, short interruptions on redundancy events, live order activity for analytics without hurting prod: redesign DB layer (read replicas, Multi-AZ, ...)
2. M4 ride-hailing highly scalable data store: instant trip status updates, near-real-time demand analytics, tamper-proof audit log of booking changes: notifications + analytics + audit (DynamoDB Streams + ...)
3. M5 healthcare: unexpected config changes, slowdowns, inconsistent patching, regulated: monitoring + auditing + compliance + automation tool combination
4. M5 startup unexpected charges after free usage: cost visibility, spending limits, accountability, optimization (Billing, Budgets, Cost Explorer, Trusted Advisor)
5. M1/M6 financial services: shared responsibility confusion, misconfigured access policies, encryption, key handling, compliance
### Fall 2025-26, A2+TA2 (5 x 10)
1. M4 real-time patient vitals (wearables): suitable Amazon database service, justify (DynamoDB-type) for performance/scale/low latency
2. M4 Nirmaan B2B e-commerce: relational DB layer, managed DB capabilities per goal (scalability, availability, security)
3. M5 fintech trading microservices on EC2: unauthorized access + data inconsistencies: AWS monitoring + security services, anomaly detection, automated alerts
4. M5 university lab Free Tier overrun: Billing and Account Management, Budgets, Cost Management tools, Trusted Advisor
5. M6 online learning platform on RDS + ALB: encrypt at rest and in transit with centralized auditable key management (KMS); WAF/Shield against SQLi, XSS, bots, volumetric spikes
### Fall 2024-25, F1+TF1 (5 x 10, partly scrambled text)
1. M3 VPC for 2-tier HA/scalable app: isolated subnet with restricted outbound internet, another with outbound internet, controlled/monitored traffic between public and private, private instances reach internet for updates (NAT)
2a. M3 video streaming latency for SE Asia/Australia: CloudFront service and benefits / 2b. M3 on-prem financial data center to VPC, low latency + secure + reliable: Direct Connect, with diagram [5]
3. M4 social media platform: high-velocity data (profiles, followers, posts, messages), delays at peak: suitable AWS database (DynamoDB)
4. M5 fleet management microservices on EC2 slow/unresponsive: AWS monitoring service (CloudWatch) to detect bottlenecks and alert
5. M5 telemedicine startup rising costs/inconsistent performance/compliance: suitable AWS service for insight and best practices (Trusted Advisor)
### Fall 2024-25, F2+TF2 (5 x 10, partly scrambled text)
1. M3 VPC design: IP range selection, 4 subnets with 251 IPs each (/24), route tables, gateways, security + cost efficiency
2. M3 global gaming platform: CloudFront + S3 multi-Region geo-proximity model with configuration steps
3. M4 financial institution on-prem DB -> managed service, 30,000 IOPS (15,000 reads/writes), not more than single writer: suitable Amazon DB service (Aurora), read replica configuration steps
4. M4 multiplayer leaderboard: high write throughput, low latency: DynamoDB, data modelling, pros
5. M5 identify AWS service to investigate unauthorized access attempts (CloudTrail), ways of event recording/access, cost-saving and best-practice service (Trusted Advisor)
### Fall 2025-26, G1 and G2 CAT-2 (PARTIAL: only first questions read; rest pending)
- G1 Q1 M3 VPC peering between two departments' VPCs: steps + SG rules; compare Site-to-Site VPN vs peering; limitation; diagram of both
- G1 Q2 M4 RDS Multi-AZ + read replicas combined for exam-period read surge; diagram
- G2 Q1 M3 NACL configuration with rule tables for public (10.0.1.0/24) and admin (10.0.2.0/24) subnets with specific allowed/denied ports and source ranges
- G2 Q2 M4 digital banking RDS outages/performance redesign (text not yet read further)

## Not yet indexed
- CAT-1 papers (AWS/PYQ/CAT1): mostly answer keys/scans; low priority
- Rest of G1/G2 CAT-2 papers
