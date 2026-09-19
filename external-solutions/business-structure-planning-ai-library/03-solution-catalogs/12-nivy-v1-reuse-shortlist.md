# Nivy V1 — Reuse-First Implementation Shortlist

**Target:** Launch a working digital-marketing agency revenue engine quickly.

## V1 outcome

Lead discovery → research → qualification → outreach → follow-up → meeting → proposal → close → revenue tracking.

## Existing assets to inspect before building

| Capability | First assets to inspect | Build from scratch? |
|---|---|---|
| Market/company research | UnifAPI Lead & Company Research Agent; existing Nivy research agents | No, unless a missing adapter exists |
| SEO/GEO | UnifAPI SEO + AI Visibility agents | No |
| Competitive intelligence | UnifAPI Competitive Intelligence Agent | No |
| Social listening | UnifAPI Social Listening Agent | No |
| Content/social | SaaS Marketing Agents; Loopmark Agent | No |
| Lead qualification | Mesh Pilot AI Sales Agent; Sales-Outreach | No |
| Personalized outreach | Mesh Pilot AI Sales Agent; Sales-Outreach | No |
| CRM workflows | n8n CRM workflow catalog | No |
| Email/calendar automation | n8n workflow library | No |
| CRM data backbone | Existing Nivy CRM work or Odoo | Decide before custom CRM build |
| AI workflow runtime | Dify for fast visual workflows; LangGraph where code/state control is required | No immediate custom runtime |
| Internal dashboard | Existing Nivy UI/agent interface; Appsmith as rapid fallback/reference | Minimize custom UI |
| Company knowledge | Existing Nivy knowledge/research + AnythingLLM/Dify/Open WebUI patterns | No custom RAG first |
| Proposal generation | Existing business skills + Nivy proposal templates | Only missing pieces |
| Social/company presence | Existing marketing skills and reusable content workflows | No custom social engine |
| Task tracking | Existing Nivy workflow/task system | No duplicate task platform |

## V1 build rule

**Reuse existing Nivy assets first. Then reuse external assets. Then adapt. Only then build missing components.**

Do not clone whole external repositories into the Nivy application by default. Preserve source URLs and licenses in the library, and create thin adapters/configurations where possible.

## V1 release gate

V1 is launch-ready when the system can support a real prospect through:

1. Research
2. Qualification
3. CRM record
4. Personalized outreach draft
5. Human approval
6. Send
7. Follow-up
8. Meeting
9. Proposal
10. Won/Lost
11. Revenue record
12. Basic KPI/report

The goal is **revenue generation**, not maximum agent count.
