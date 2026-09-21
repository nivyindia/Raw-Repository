# Final Gap Discovery — Ad Allocation, Causal KPI, Capacity, Board, Procurement, CHRO & Digital Twin — September 2026

## Purpose

This batch attacks the seven explicit gaps left by Catalog 29:

1. Cross-platform autonomous advertising allocator
2. Cross-company causal KPI/root-cause engine
3. Enterprise AI capacity planner
4. Autonomous board/executive agent
5. Complete AI Procurement executive
6. Complete AI CHRO executive
7. Company-wide Digital Twin runtime

Principle:

**DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING**

All entries are reuse/discovery candidates. Repository claims are not production evidence; verify license, maintenance, security, interfaces, data quality and runtime behavior before adoption.

---

## 1. Cross-platform autonomous advertising allocation

### Strong candidates

| Resource | Type | What it adds | Reuse role | Source |
|---|---|---|---|---|
| Marketing Orchestrator LLM | Open-source MIT | Omnichannel orchestration across Google, Meta, TikTok, Snap, LinkedIn, Amazon DSP, WhatsApp, email, SMS and calls; real-time budget reallocation, counterfactual planning and policy-as-code approvals | Closest match to Nivy cross-platform allocator | https://github.com/Crynge/marketing-orchestrator-llm |
| AdVantage | Open-source | ML-driven budget allocation, creative prediction and automated bidding across Google, Meta, TikTok and DV360 | Multi-platform optimization reference | https://github.com/Crynge/AdVantage |
| AdOps MCP | Open-source | CSV-first Google + Meta analysis, anomaly detection, budget allocation, A/B significance and forecasting | Low-friction analytics/optimization adapter | https://github.com/automatiabcn/adops-mcp |
| Meta Ads MCP | Open-source/free service | AI campaign analysis, budget optimization recommendations and automated monitoring for Meta | Platform adapter | https://github.com/pipeboard-co/meta-ads-mcp |
| Oransim | Open-source | Causal marketing simulation and counterfactual ROI prediction with inspectable causal graph | Experiment/simulation layer | https://github.com/OranAi-Ltd/oransim |

The Marketing Orchestrator LLM is the strongest architectural match because it explicitly combines omnichannel control, real-time budget reallocation, counterfactual simulation and policy approvals. AdVantage provides another concrete optimization implementation. cite-turn0search17 cite-turn0search6

### Nivy decision

**Gap status: PARTIALLY CLOSED.**

Do not build an allocator from scratch yet. First qualify Marketing Orchestrator LLM + AdVantage + platform adapters.

Required Nivy contract:

**Revenue Goal → Total Budget → Channel Budget → Campaign Budget → Pacing → Attribution → Marginal Return → Reallocation Proposal → Policy Gate → Execute → Verify → Incremental Impact → Learn**

---

## 2. Cross-company causal KPI / root-cause engine

### Strong candidates

| Resource | Type | What it adds | Reuse role | Source |
|---|---|---|---|---|
| InsightAgent | Open-source | Multi-agent KPI anomaly investigation, domain decomposition, deterministic severity scoring and evidence-backed executive reports | Direct KPI RCA reference | https://github.com/Aanchalshah2007/InsightAgent |
| Causal AI Scientist / causal-agent | Open-source | Natural-language causal questions, method selection, code execution, validation and interpretation; DiD, IV, OLS, RDD, backdoor/frontdoor | Causal inference engine | https://github.com/causalNLP/causal-agent |
| Oransim | Open-source | Inspectable causal graph and counterfactual marketing simulation | Domain-specific causal simulator | https://github.com/OranAi-Ltd/oransim |
| Phoring | Open-source | Knowledge graph → multi-agent simulation → source-cited forecast | Scenario/decision intelligence reference | https://github.com/inbharatai/phoring |

InsightAgent is particularly aligned with the Nivy reporting loop because it separates deterministic computation from LLM report writing. Causal-agent adds formal causal-inference methods instead of treating correlation as causation. cite-turn1search7 cite-turn1search10

### Nivy decision

**Gap status: PARTIALLY CLOSED.**

Reuse the architecture, but do not claim generic company causality from a correlation engine.

Required layers:

**Metric Deviation → Domain Selection → Data Window → Statistical Evidence → Causal Method Selection → Hypothesis → Intervention/Experiment → Post-Intervention Measurement → Confidence → Report**

---

## 3. Enterprise AI capacity planning

| Resource | Type | What it adds | Reuse role | Source |
|---|---|---|---|---|
| AI Workforce Capacity Planning Platform | Open-source MIT | Demand forecasting, workforce requirements, capacity gaps, overtime, staffing optimization, recommendations, reporting and monitoring | Direct capacity-planning candidate | https://github.com/isskabre/AI-Workforce-Capacity-Planning-Platform |
| HR Skills | Open-source Agent Skills | Workforce planning, HR analytics, recruiting, onboarding/offboarding, performance, succession and organizational effectiveness | CHRO skills layer | https://github.com/tuanductran/hr-skills |
| Workforce Insights agent | Microsoft Frontier/reference | Skills-based workforce planning, organizational structure analysis and workforce composition | Enterprise HR planning reference | https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/workforce-insights-agent.md |
| StaffPortal | Open-source | Attendance, leave, timesheets, expenses, audit, HR support and role-based workforce data | Operational HR data source | https://github.com/sarmakska/staff-portal |

The capacity-planning platform explicitly implements the chain **demand forecasting → workforce capacity planning → staffing/overtime optimization → decision orchestration → reporting/monitoring**. cite-turn0search2

### Nivy decision

**Gap status: CLOSED AT COMPONENT LEVEL; INTEGRATION GAP REMAINS.**

Use an existing capacity engine rather than building forecasting/optimization from scratch. Nivy still needs to connect capacity to projects, tasks, AI employees, skills, cost and company-wide demand.

---

## 4. Autonomous board / executive agent

| Resource | Type | What it adds | Reuse role | Source |
|---|---|---|---|---|
| TAI Chief / AI Chief of Staff | Open-source MIT | Executive command center, department dashboards, board-ready decisions, company digital twin, scenario simulation, PDF reports and board memos | Strongest Nivy executive-layer candidate | https://github.com/suhasbhairav/ai-chief-of-staff |
| AgentBoardroom | Open-source | CEO/CTO/QA/Auditor governance, decision lineage, challenge gates, budget monitoring, emergency stop and persistent audit trail | Governance/board-control pattern | https://github.com/GixGosu/AgentBoardroom |
| Board Observer | Open-source | Board meeting preparation, live transcription, decisions, action items and post-meeting governance | Meeting intelligence layer | https://github.com/vitalii-dynamiq/board-observer |

TAI Chief is unusually close to the Nivy target because it combines department metrics, executive scorecards, board memos, a company digital twin and scenario simulation. cite-turn1search1 AgentBoardroom adds explicit governance gates and decision lineage. cite-turn0search4

### Nivy decision

**Gap status: CLOSED AT REFERENCE-ARCHITECTURE LEVEL.**

Do not build a separate board application. Compose the board layer from:

**Digital Twin + KPI Engine + Scenario Engine + Decision Inbox + Governance/Audit + Board Memo/Report Generator.**

---

## 5. Complete AI Procurement executive

| Resource | Type | What it adds | Reuse role | Source |
|---|---|---|---|---|
| Autonomous Procurement Agent | Open-source MIT | Supplier discovery, quote negotiation, offer comparison, exception handling, vector memory and REST integration | Procurement execution reference | https://github.com/kashewknutt/autonomous-procurement-agent |
| ProofPay | Open-source MIT | Goal + budget → provider → contract → escrow → delivery proof → deterministic payment/dispute gate | Strong governed autonomous transaction pattern | https://github.com/JafCR/ProofPay |
| Procurement Optimization | Open-source | Spend classification, sourcing optimization, supplier optimization, contract analysis and purchasing workflows | Procurement analytics layer | https://github.com/virbahu/procurement-optimization |

The Autonomous Procurement Agent covers supplier discovery, negotiation, quote comparison and exception handling. ProofPay demonstrates a stronger safety pattern: the LLM can recommend/veto, but deterministic policy code controls money release. cite-turn0search0 cite-turn0search9

### Nivy decision

**Gap status: PARTIALLY CLOSED.**

The execution layer exists in reusable form. A full AI Procurement executive still needs spend governance, category strategy, supplier risk, budget authority, contract lifecycle, three-way match and executive reporting.

---

## 6. Complete AI CHRO executive

| Resource | Type | What it adds | Reuse role | Source |
|---|---|---|---|---|
| OpenWorker | Open-source | AI-worker identity, onboarding, roles, permissions, supervision, evaluation, promotion, suspension and retirement | AI workforce HR/control layer | https://github.com/openworker-io/openworker |
| HR Skills | Open-source Agent Skills | Employee lifecycle, workforce planning, performance, succession, compensation, learning and HR analytics | CHRO skill library | https://github.com/tuanductran/hr-skills |
| AI-HR-Agent | Open-source | HCM search/update through natural language, employee/candidate lookup, record creation/update and human approval | HR system agent adapter | https://github.com/Saiko-Seiko/AI-HR-Agent |
| StaffPortal | Open-source | Attendance, leave, timesheets, expenses, audit and workforce support | HR operational system | https://github.com/sarmakska/staff-portal |

OpenWorker is especially important for Nivy because it models AI agents as governed workers with lifecycle states and permissions. cite-turn0search5 The HR Skills project expands the domain coverage into workforce planning, performance and succession. cite-turn1search13

### Nivy decision

**Gap status: CLOSED AT COMPONENT LEVEL; FULL CHRO COMPOSITION REMAINS.**

Use:

**HRIS + HR Skills + OpenWorker + workforce capacity engine + performance/KPI layer + identity/RBAC**

instead of creating a monolithic CHRO application.

---

## 7. Company-wide Digital Twin runtime

### Strong candidates

| Resource | Type | What it adds | Reuse role | Source |
|---|---|---|---|---|
| TAI Chief | Open-source MIT | Company digital twin, department snapshots, executive rollups and scenario simulation | Closest company-level reference | https://github.com/suhasbhairav/ai-chief-of-staff |
| Utopia | Open-source | Time-aware enterprise world model, ontology, conflict detection, reasoning, decision support, MCP and offline deployment | Canonical knowledge/world-model candidate | https://github.com/deeplethe/utopia |
| Digital Twin System Framework | Open reference architecture | Data → Context → Decision/Process Orchestration → Actuation architecture for digital-twin systems | Governance/architecture standard | https://github.com/digitaltwinconsortium/digital-twin-system-framework |
| OFacT | Open-source | State model, data integration, simulation, scenario generation, optimization and KPI analytics | Digital-twin runtime/reference | https://github.com/OpenFactoryTwin/ofact |
| AIRA | Open-source prototype | Multi-agent operations + digital twin simulation + MCP + human approval | Closed-loop decision pattern | https://github.com/karthikmanikandan/AIRA-Autonomous-Manufacturing-Decision-Platform |
| ORION | Open-source | Digital twin + multi-agent detect/diagnose/plan/safety/approval/execute/verify pipeline | Self-healing twin pattern | https://github.com/L-N-X-1/ORION |

Utopia is a particularly interesting candidate for the **semantic/knowledge substrate**, while TAI Chief is closer to the **company-executive UX and digital-twin application**. The Digital Twin System Framework provides a useful architecture for connecting context, decisions and actuation. cite-turn1search8 cite-turn1search1 cite-turn1search12

### Nivy decision

**Gap status: CLOSED AT ARCHITECTURE LEVEL; NO SINGLE DROP-IN COMPANY TWIN FOUND.**

The correct strategy is composition, not a giant new platform.

---

# 8. Final seven-gap status

| Original gap | Result | Reuse first |
|---|---|---|
| Cross-platform ad allocator | **Partially closed** | Marketing Orchestrator LLM + AdVantage + platform MCP/API adapters |
| Causal KPI engine | **Partially closed** | InsightAgent + causal-agent + domain-specific causal models |
| Enterprise capacity planner | **Closed at component level** | AI Workforce Capacity Planning Platform + HR Skills |
| Autonomous board agent | **Closed at reference architecture** | TAI Chief + AgentBoardroom |
| AI Procurement executive | **Partially closed** | Autonomous Procurement Agent + ProofPay + Procurement Optimization |
| AI CHRO executive | **Closed at component level** | OpenWorker + HR Skills + HRIS + capacity/performance systems |
| Company Digital Twin runtime | **Closed at architecture level** | TAI Chief + Utopia + Digital Twin System Framework + simulation components |

---

# 9. New Nivy master architecture

The seven gaps converge into one architecture:

**DATA SOURCES**
↓
**INTEGRATION / MCP / API / BROWSER**
↓
**UNIVERSAL DATA MODEL**
↓
**DIGITAL TWIN / WORLD MODEL**
↓
**DEPARTMENT + WORKFORCE GRAPH**
↓
**KPI / METRIC / CALCULATION ENGINES**
↓
**CAUSAL + FORECAST + SIMULATION ENGINES**
↓
**AI EXECUTIVE / DEPARTMENT HEAD**
↓
**PLAN / WORKFLOW / AGENT RUN**
↓
**POLICY / BUDGET / RISK GATE**
↓
**HUMAN APPROVAL WHEN REQUIRED**
↓
**EXECUTION**
↓
**VERIFICATION**
↓
**OUTCOME / KPI IMPACT**
↓
**AUDIT / REPLAY**
↓
**LEARNING / DIGITAL-TWIN UPDATE**

This makes advertising, finance, HR, procurement, sales and IT variations of the same company operating system rather than separate applications.

---

# 10. Important reusable design rules discovered

### Rule 1 — LLM is not the calculator

Financial and KPI numbers must come from deterministic calculations or validated analytical engines.

### Rule 2 — LLM is not the payment authority

ProofPay demonstrates a strong pattern: policy code controls payment release; the model cannot force payment. cite-turn0search9

### Rule 3 — Causality requires evidence

KPI RCA should distinguish:

**Observed → Correlated → Hypothesized → Tested → Causally supported**

### Rule 4 — Every autonomous action needs lineage

Store:

**Input → Evidence → Model/Agent → Decision → Policy → Approval → Action → Result → Verification**

### Rule 5 — Digital Twin is semantic infrastructure

It should not merely be a dashboard or 3D model.

### Rule 6 — Department heads share one protocol

Every AI executive should emit:

**Goal → Plan → Run → Task → Evidence → KPI → Recommendation → Risk → Approval → Action → Outcome → Audit**

---

# 11. Remaining true build gaps

After this discovery batch, the remaining gaps are narrower:

1. **Nivy Universal Data Model** — normalize CRM, ERP, HR, ads, finance, projects, IT and AI-workforce objects.
2. **Nivy Digital Twin integration layer** — connect the reusable world-model/twin candidates.
3. **Cross-company causal graph** — combine KPI, event, process and intervention evidence.
4. **Nivy policy/approval engine** — unify budget, risk, identity and human approval gates.
5. **Cross-platform attribution contract** — normalize revenue attribution across advertising channels.
6. **Company-wide scenario engine** — simulate cross-department consequences before major actions.
7. **Unified executive/employee UI** — expose all of the above through the existing one-workspace model.

These are integration/composition problems first. The discovery evidence does **not** justify building seven separate systems.

**Status: FINAL GAP DISCOVERY COMPLETE.**
