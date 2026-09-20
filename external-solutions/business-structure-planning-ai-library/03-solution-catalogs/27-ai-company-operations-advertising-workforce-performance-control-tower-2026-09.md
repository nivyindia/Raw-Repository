# AI Company Operations, Advertising, Workforce Performance & Control-Tower Reuse Catalog — September 2026

## Purpose

The existing library covers agents, departments, unified UI, AI technology, memory, governance and BI. This catalog adds the continuous company-operating layer:

**RUN → MEASURE → REPORT → DETECT → EXPLAIN → FIX → APPROVE → ACT → VERIFY → LEARN**

Scope: AI-operated advertising, campaign reporting and optimization; department KPI reporting; human and AI employee performance; task/workflow/SLA monitoring; errors/incidents/retries/RCA; cost/token/latency monitoring; executive control towers; scheduled reports and alerts; BI; governance and audit.

**Reuse rule:** candidates are not automatic adoption decisions. Verify current source, license, API access, data model, deployment, security and runtime behavior before integration.

## 1. Advertising operations

| Resource | Type | Relevant capability | Reuse role | Source |
|---|---|---|---|---|
| Campawn | Open-source | Dashboard-first campaign planning; Google/Meta/Amazon creation; ReportingAgent; OptimizationAgent; memory; human approval; retries; typed errors | Multi-platform advertising control-plane reference | https://github.com/dimzachar/campawn |
| Shogo AI Ad Campaign Reporting | Commercial | Spend, CTR, CPC, ROAS and conversion reporting; live dashboard; budget pacing alerts; campaign health; client reporting | Ad-reporting reference | https://shogo.ai/use-cases/ad-campaign-reporting/ |
| Google Ads API | Platform API | Campaign management, budgets, bidding, ads, conversions and reporting | Direct connector | https://developers.google.com/google-ads/api |
| Meta Marketing API | Platform API | Campaign/ad-set/ad management, insights and budgets | Direct connector | https://developers.facebook.com/docs/marketing-apis/ |
| Amazon Ads API | Platform API | Sponsored advertising campaign management and reporting | Direct connector | https://advertising.amazon.com/API |
| LinkedIn Marketing APIs | Platform API | Advertising/campaign and reporting integrations subject to permissions | Connector candidate | https://learn.microsoft.com/linkedin/marketing/ |

Required Nivy loop:

**Brief/goal → audience → budget → media plan → human approval → platform payload → launch → collect metrics → normalize → calculate KPI → anomaly detection → recommendation → approval gate → optimization → report → learn.**

Normalize: spend, impressions, reach, clicks, CTR, CPC, CPM, conversions, CVR, CPA/CPL, revenue, ROAS, frequency, budget pacing, attribution window and creative signals.

High-impact changes should pass the Nivy policy/approval layer rather than being auto-applied simply because an AI recommends them.

## 2. AI-agent observability, performance and error resolution

| Resource | Type | Relevant capability | Reuse role | Source |
|---|---|---|---|---|
| Langfuse | Open-source | Tracing, tool-call visibility, evaluations, experiments, prompts, cost/latency dashboards and alerts | Primary observability candidate | https://langfuse.com/ |
| Agent Monitor | Open-source | Real-time traces, task flows, tool calls, cost/token tracking, latency, throughput, errors, retries, replay, alerts and dashboards | Lightweight monitoring candidate | https://github.com/cogniolab/agent-monitor |
| AgentObserve | Open-source | Agent fleet runs/traces, cost budgets, regression detection, SLA scoring, incidents and routing | Fleet operations reference | https://github.com/mizcausevic-dev/agentobserve |
| AgentLens | Open-source | LLM/tool/decision traces, cost anomaly detection, prompt diffs, real-time dashboard and audit | Observability candidate | https://github.com/Nitin-100/agentlens |
| AgentLens MCP-native | Open-source | OTel GenAI, MCP, tamper-evident events, live dashboard, cost/latency/error alerts, replay and health views | Audit/trace candidate | https://github.com/agentkitai/agentlens |
| Argus | Open-source | OTel traces, analytics, behavioral issue detection, tool loops/errors, runaway tokens and alerts | Local-first observability candidate | https://github.com/mylesndavid/argus |
| Tracea | Open-source | Session tracking, real-time dashboard, issue rules, high-cost/high-latency detection, loops, AI RCA and alert routing | Error-resolution/RCA candidate | https://github.com/darshannere/tracea |
| Agent Observability | Open-source | Tool-call audit, session grading, token/cost tracking, dashboard and historical analytics | Local agent telemetry candidate | https://github.com/KryptosAI/agent-observability |
| Flightdeck | Open-source | Live agent fleet, event timeline, agent dashboard, token/latency/error/cost trends and event search | Fleet dashboard reference | https://github.com/flightdeckhq/flightdeck |
| Agent Dashboard | Open-source | Agent health, work queue, retry/cancel, schedules, failures, logs, pipelines and P50/P95/P99 metrics | Local operator-console reference | https://github.com/brunokktro/agent-dashboard |

Core Nivy observability model:

**Agent → Run → Step → Tool Call → External System → Result → Error/Retry → Cost → KPI → Incident → Root Cause → Resolution → Verification**

Track at minimum: success/failure rate; error classes; retry rate; task completion; SLA/SLO; latency P50/P95/P99; token/cost; API failures; loops; quality/evaluation score; human override rate; business outcome; availability; queue age; incidents; MTTR.

## 3. Human + AI employee / workforce performance

| Resource | Type | Relevant capability | Reuse role | Source |
|---|---|---|---|---|
| NiCE Performance Management | Commercial | Unified dashboards/reporting for human and AI workforce; KPI tracking across front/mid/back office; compare human and AI outcomes | Enterprise workforce-performance reference | https://www.nice.com/products/performance-management |
| HubOS | Open-source | Specialized AI employees with identity, skills, memory, dispatcher and multi-channel execution | AI workforce architecture reference | https://github.com/hubos-ai/HubOS |
| Horizon Dashboard | Platform | Active agents, completed tasks, token usage, error rate, response time and business-health KPI views | Control-tower UX reference | https://docs.horizonplatform.ai/platform/dashboard/overview/ |

Nivy employee-performance model:

**Identity → Role → Department → Manager → Responsibilities → Skills → Assigned Work → Queue → SLA → Output → Quality → KPI → Cost → Availability → Errors → Escalations → Reviews → Learning**

Human HR metrics and AI-agent operational metrics should share a common performance contract but retain separate privacy, policy and governance controls.

## 4. Department reporting and executive control tower

Hierarchy:

**Company → Division → Department → Team → Human Employee / AI Employee → Workflow → Task → Action**

Every department should expose a common reporting contract:

| Layer | Examples |
|---|---|
| Objectives | annual/quarterly objectives, OKRs |
| KPIs | target, actual, variance, trend |
| Work | assigned, running, blocked, completed, overdue |
| Quality | defects, rework, QA score, customer impact |
| Productivity | output/hour, cycle time, throughput |
| Financial | revenue, cost, margin, budget, variance |
| People | capacity, utilization, workload, skills gaps |
| AI workforce | runs, success, cost, quality, exceptions |
| Risk | incidents, policy violations, unresolved risks |
| SLA | breached, at-risk, achieved |
| Customer | satisfaction, retention, complaints, outcomes |
| Forecast | expected result vs target |
| Actions | recommendations, approvals, owners, due dates |
| Audit | evidence, source, timestamp, actor |

Roll-up must be automatic:

**Task → Employee → Team → Department → Executive → Company**

The same metric should not be manually re-entered into separate reports.

## 5. BI and reporting systems

| Resource | Type | Relevant capability | Reuse role | Source |
|---|---|---|---|---|
| Metabase | Open-source BI | Dashboards, query builder, reporting, permissions, embedding and AI data capabilities | Fast internal BI candidate | https://www.metabase.com/ |
| Apache Superset | Open-source BI | Dashboards, datasets, charts and MCP-based AI interaction | Scalable BI candidate | https://superset.apache.org/ |
| Helical Insight | Open-source BI | AI conversational analytics, dashboards, scheduled/paginated reporting, embedding, SSO, multi-tenancy and row-level security | Reporting-heavy BI candidate | https://github.com/helicalinsight/helicalinsight |
| Lightdash | Open-source BI | Semantic-model-driven analytics and dashboards | Analytics candidate | https://github.com/lightdash/lightdash |
| Redash | Open-source BI | Querying, visualization and dashboards | Lightweight analytics candidate | https://github.com/getredash/redash |
| Grafana | Open-source observability/analytics | Operational dashboards, metrics, alerting and integrations | Infrastructure/operations dashboard layer | https://grafana.com/ |

BI tools should be presentation/query layers, not the canonical company data model. The Nivy digital twin and universal data contracts remain Nivy-owned.

## 6. Autonomous reporting and intelligence

A reusable reporting agent should:

1. ingest ERP/CRM/ad/project/HR/support/agent telemetry data;
2. normalize metrics;
3. calculate derived KPIs;
4. compare target vs actual;
5. detect anomalies;
6. identify probable causes;
7. produce department report;
8. produce executive summary;
9. create recommended actions;
10. route approvals;
11. distribute to permitted recipients;
12. record delivery/audit evidence;
13. monitor whether actions changed the KPI.

Report types: real-time dashboard; hourly operational report; daily department report; weekly management report; monthly business review; quarterly business review; campaign report; human/AI-worker performance; project; financial; SLA; incident; risk; customer health; sales pipeline; marketing attribution; executive/company; board-style.

## 7. Error detection → diagnosis → resolution

**Detect → classify → correlate → reproduce → diagnose → propose fix → approval/policy gate → remediate → verify → close → learn**

Error classes: application/runtime; API/authentication; rate limit; data quality; workflow; integration; model/LLM; tool selection; prompt/context; retrieval/RAG; policy/security; cost/budget; performance/latency; infrastructure; human process; external platform; business-rule violation.

| Level | Example | Automation |
|---|---|---|
| L0 | Log/notify | Automatic |
| L1 | Retry/backoff | Automatic within policy |
| L2 | Restart/requeue | Automatic within policy |
| L3 | Switch provider/model/route | Policy-controlled |
| L4 | Roll back workflow/prompt/config | Approval depending on impact |
| L5 | Pause agent/campaign/payment/action | Human approval by default |
| L6 | Cross-system business remediation | Human approval by default |

## 8. Nivy control-tower architecture

`Data Sources → Integration Layer → Universal Data Model → AI Intelligence → Governance → Execution → Verification → Nivy Experience`

Data sources: ERP, CRM, Ads, Email, Social, HR, Finance, Projects, Support, Agent Telemetry.

Integration: API, webhook, MCP, A2A, browser automation, n8n and ETL.

Universal objects: Company, Department, Person, AI Employee, Customer, Campaign, Project, Task, KPI, Incident, Cost, Action, Outcome, AuditEvent.

AI intelligence: Analyst Agent, Reporting Agent, Forecast Agent, Anomaly Agent, RCA Agent, Optimization Agent.

Governance: Identity, RBAC, Policy, Budget, Approval, Audit.

Execution: Workflow, Agent, Tool, Platform API.

Verification: Result, KPI delta, evidence and audit.

Experience: Nivy Executive Dashboard, Department Dashboard, Manager Dashboard, Employee Dashboard and AI Operator Dashboard.

## 9. Required dashboard surfaces

**Company/CEO:** revenue, profit, cash, pipeline, marketing, sales, operations, people, AI workforce, projects, risks, incidents, customer health, system health and strategic KPIs.

**Department Head:** objectives, department KPIs, budget, workload, team performance, AI employees, bottlenecks, SLA, incidents, risks and actions.

**Manager:** team queue, individual workloads, overdue tasks, quality, output, exceptions, approvals and coaching/review signals.

**Employee:** my work, priorities, deadlines, KPIs, feedback, documents, approvals, learning and alerts.

**AI Operator/Manager:** active agents, queued jobs, failed runs, retries, tool/API health, cost, latency, quality, policy events, approvals, incidents and recommended interventions.

**Client:** approved campaign/project KPIs, deliverables, reports, invoices and communication; never internal workforce/governance data.

## 10. What this adds to the library

The earlier catalogs describe what the company and AI technology universe contains. This catalog adds the missing **continuous operating/control loop**:

**Operate → Observe → Report → Calculate → Compare → Detect → Diagnose → Resolve → Approve → Execute → Verify → Learn**

Nivy therefore needs a cross-company **AI Operations & Performance layer**, not merely separate marketing/HR/sales agents.

Build reusable contracts/adapters for:

`Metric`, `KPI`, `Report`, `Dashboard`, `Run`, `Task`, `Incident`, `Error`, `Alert`, `Recommendation`, `Approval`, `Action`, `Outcome`, `AuditEvent`, `PerformanceRecord`.

Any department, employee, AI employee, campaign, project or system should plug into the same control plane.

## 11. Initial Nivy reuse shortlist

| Capability | Candidates to inspect | Nivy ownership |
|---|---|---|
| Multi-platform ads | Campawn + official platform APIs | Universal campaign contract + approval |
| Ad reporting | Shogo pattern + platform APIs | Normalized campaign metrics |
| Agent observability | Langfuse / AgentObserve / AgentLens | Common telemetry contract |
| Agent error/RCA | Tracea / Argus | Incident + remediation contract |
| AI workforce performance | NiCE / Horizon / HubOS patterns | AI-employee performance model |
| BI dashboards | Metabase / Superset / Helical Insight | Unified Nivy shell + permissions |
| Operational metrics | Grafana | Common metric/alert contract |
| Governance | Existing AGT/A2A candidates | Policy/approval/audit contract |

Do not choose a single winner yet. Run qualification tests against Nivy contracts and keep replaceable adapters.

## 12. Discovery gaps

Continue researching: direct autonomous Google/Meta/LinkedIn/Amazon campaign optimization; creative generation/testing/budget allocation; cross-platform attribution and MMM; autonomous media buying with approvals; department-specific AI CFO/CHRO/COO/CMO reporting; workforce capacity planning; AI employee KPI management; autonomous incident remediation; AI SRE/IT operations; agent fleet scheduling; cross-company anomaly detection; causal/RCA across departments; predictive KPI forecasting; board reporting; real-time digital-twin control towers; privacy-preserving employee analytics; compensation workflows; agent benchmarking; AI FinOps; unified alert/escalation; evidence graphs; report fact checking; report lineage and metric provenance.

**Status:** Discovery catalog. Runtime qualification is required before production reuse.