# 51 — High-Demand International AI Agent Service Catalog

Purpose: expand discovery beyond departments into client-facing AI services that can be packaged and sold internationally.

## Priority service families

| Priority | Agent / system | Typical job | Channels | Reuse candidates | Human approval |
|---|---|---|---|---|---|
| P0 | AI Receptionist | Answer calls, FAQ, routing, messages, transfers | Phone/SIP | AIReceptionist; AIVA; VoiceAgent | Yes for sensitive/escalation cases |
| P0 | AI Chatbot / Website Concierge | Qualify visitors, answer FAQs, capture leads, book meetings | Website/chat | Front-office agent platforms; MCP tools | Yes for uncertain/high-risk answers |
| P0 | AI Appointment Setter | Qualify prospects and schedule meetings | Voice/web/chat | AI voice appointment setter; VoiceAgent | Yes before final booking if needed |
| P0 | AI SDR / BDR | Research accounts, qualify leads, draft outreach, follow-up | Email/LinkedIn/WhatsApp/Telegram | GTM Skills; B2B SDR templates | Yes before external send initially |
| P0 | Customer Support Agent | FAQ, ticket triage, response drafting, escalation | Email/chat/helpdesk | Anthropic customer-support plugin; support agents | Yes for refunds/legal/complex cases |
| P0 | Lead Qualification Agent | Intake, qualification, routing, CRM update | Web/forms/chat/voice | SDR/voice agent patterns | Yes for scoring policy |
| P1 | Sales Follow-up Agent | Monitor pipeline, reminders, follow-ups, dormant-lead revival | CRM/email/chat | n8n + CRM + GTM skills | Approval for outbound until proven |
| P1 | Proposal / RFP Agent | Read requirements, build compliance matrix, draft proposal | Email/portal/docs | Research + document skills | Mandatory final review |
| P1 | AI Recruiting Agent | JD intake, resume extraction, candidate communications, scheduling | ATS/email | Recruiter-agent projects | Human hiring decision mandatory |
| P1 | AI Executive Assistant | Inbox, calendar, research, reminders, briefing | Email/calendar/chat | Assistant, GAIA, OpenClaw-style systems | Approval for consequential actions |
| P1 | AI Research Agent | Market/account/competitor research and reports | Web/docs | Deep-research agent patterns | Review sources |
| P1 | AI Knowledge Agent | Internal company Q&A and document retrieval | Slack/Teams/web | RAG/MCP/enterprise-search | Access controls |
| P1 | AI Operations Agent | Monitor workflows, exceptions, tasks and deadlines | Email/Slack/Telegram/CRM | n8n + agent orchestration | Approval for destructive actions |
| P1 | AI Social Media Agent | Strategy, content, repurposing, publishing, analytics | Social channels | Social Media Skills; Marketing OS | Human approval for publishing initially |
| P1 | AI Review/Reputation Agent | Monitor reviews, draft responses, identify issues | Google/social/review platforms | Social/reputation workflows | Human approval for negative/escalated responses |
| P2 | AI Finance Operations Agent | AR follow-up, reconciliation support, close checklists | Email/accounting/ERP | Finance skills | Finance professional approval |
| P2 | AI Legal Intake Agent | Intake, classify documents, summarize, route | Email/forms/docs | Legal skill libraries | Lawyer review; not autonomous legal advice |
| P2 | AI IT Helpdesk Agent | Triage incidents, knowledge lookup, ticket creation | Chat/email/ITSM | ITSM/MCP workflows | Privileged actions gated |
| P2 | AI Procurement Agent | Vendor research, quote comparison, renewal reminders | Email/docs/ERP | Procurement workflows | Approval before purchasing |
| P2 | AI Localization Agent | Translate/localize content and support | Web/docs/chat | Translation/localization workflows | Human linguistic/legal review where required |
| P2 | AI Training Agent | Onboarding, quizzes, SOP coaching, knowledge checks | LMS/chat | Skills + knowledge base | Human curriculum owner |

## Concrete current sources

- AIReceptionist — self-hosted phone receptionist; inbound calls, FAQ, transfers, messages, after-hours handling. AGPL-3.0. https://github.com/kirklandsig/AIReceptionist
- AIVA — open-source voice receptionist for calls, appointments, orders and FAQs; multilingual. https://github.com/7XLabs/Aiva
- VoiceAgent — open-source phone-agent platform for inbound calls, appointment scheduling, lead capture and FAQ handling. https://github.com/homgorn/real-voice-agent-free
- AI Voice Appointment Setter — voice qualification/scheduling template with specialist agents and guardrails. https://github.com/suhasbhairav/ai-voice-appointment-setter
- B2B SDR Agent Template — open-source SDR architecture across WhatsApp, Telegram and email. https://github.com/iPythoning/b2b-sdr-agent-template
- Assistant — self-hosted assistant with email interface, web research, scripts, scheduling and recurring reminders. Apache-2.0. https://github.com/rb81/assistant
- GAIA — proactive multi-channel assistant with workflows, memory, calendar, smart todos and integrations. https://github.com/theexperiencecompany/gaia
- Owl Agent — Telegram assistant with task decomposition, document processing and smart reminders. MIT. https://github.com/MarcusMQF/owl-agent
- OpenClaw — multi-channel assistant architecture with skills, memory and many chat channels. https://github.com/Glucksberg/OpenClaw
- AI Recruiter — open-source recruitment agent examples for screening, sourcing and outreach. https://github.com/Ismail-2001/agent-recruiter

## Nivy packaging opportunities

1. AI Receptionist as a monthly managed service.
2. Website AI Concierge + lead qualification + booking.
3. AI SDR / outbound appointment-setting system.
4. Customer-support automation package.
5. AI Recruiting Desk for SMBs.
6. AI Executive Assistant / Founder Office.
7. AI Proposal/RFP Desk.
8. AI Review and Reputation Desk.
9. AI Operations + reminder/control-room system.
10. Vertical bundles: clinics, home services, accounting firms, agencies, recruitment firms, restaurants/hospitality, professional services.

## Safety / adoption rule

Treat third-party agents as reusable components, not automatically trusted production software. Verify license, dependencies, security, credentials, data handling, platform terms, and approval gates before deployment. Keep humans in the loop for hiring decisions, legal/accounting judgments, payments, sensitive customer actions and consequential communications.