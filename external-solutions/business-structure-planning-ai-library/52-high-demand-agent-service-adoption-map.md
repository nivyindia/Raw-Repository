# 52 — High-Demand AI Agent Service Adoption Map

## P0 — Build/test first

| Service | First implementation | Success metric |
|---|---|---|
| AI Receptionist | Inbound FAQ + transfer + message capture | Answer rate, qualified calls, escalation rate |
| Website AI Concierge | Knowledge base + qualification + booking | Visitor-to-lead, lead-to-meeting |
| AI SDR | Account research + personalized draft + CRM + follow-up | Qualified meetings per 100 accounts |
| AI Appointment Setter | Voice/web qualification + calendar handoff | Qualified appointments, show rate |
| Customer Support Agent | FAQ + ticket classification + draft replies | Resolution time, escalation accuracy |
| Lead Qualification Agent | Form/chat/voice intake + CRM routing | Qualified-lead rate |

## P1 — Add after core revenue engine

- Proposal/RFP agent
- Recruiting agent
- Executive assistant
- Research agent
- Knowledge agent
- Operations/reminder agent
- Social/reputation agent

## P2 — Specialist/regulated workflows

- Finance operations
- Legal intake
- IT helpdesk
- Procurement
- Localization
- Training

## Common architecture

`Channel → Intake Agent → Knowledge/RAG → Specialist Agent → Tool/MCP/API → Approval Gate → Action → CRM/ERP → Audit Log → Follow-up`

## Productization pattern

Offer each as:
- Setup / implementation
- Monthly managed AI agent
- Usage-based add-on where appropriate
- Human escalation/QC option
- Analytics dashboard
- Continuous optimization

## International-market packaging

Prefer outcome-based packages rather than selling an AI model. Example outcomes:
- calls answered
- leads qualified
- meetings booked
- tickets resolved
- candidates processed
- proposals drafted
- reviews monitored
- follow-ups completed

## Guardrails

Outbound messaging, hiring decisions, payments, legal conclusions, financial postings, destructive system actions and sensitive customer-data operations require explicit policies and appropriate human approval.