# Revenue Channel Automation Adoption Map

## P0 — build/test first

| System | Existing asset | First implementation | Approval |
|---|---|---|---|
| Telegram control plane | n8n Telegram workflows | One Nivy bot for commands, approvals, alerts and status | Human for external actions |
| Upwork opportunity agent | citizenweb3/upwork-agent | Search -> fit score -> proposal draft -> Telegram approval -> CRM | Required before submission |
| Influence engine | InfluenceX / CreatorReach AI | Creator discovery -> outreach draft -> reply classification | Required before commitments |
| Content publisher | n8n templates | Research -> content -> creative -> approval -> publish -> log | Required for brand-sensitive content |
| Follow-up engine | n8n + CRM | Every lead/opportunity gets next-action date and escalation | Low-risk reminders can be automatic |

## P1

- Fiverr opportunity and buyer-message workflow
- RFP/procurement portal monitoring
- partner/referral discovery
- community and Telegram channel monitoring
- lead enrichment/deduplication
- automated meeting preparation

## P2

- cross-channel influence graph
- attribution from content -> conversation -> opportunity -> revenue
- adaptive channel allocation
- agent-to-agent opportunity routing
- autonomous low-risk follow-up

## Shared architecture

`Channel adapters -> Event bus/n8n -> Qualification agent -> CRM -> Specialist agent -> Approval gate -> Channel executor -> Evidence/log -> Follow-up scheduler -> Analytics`

## Safeguards

1. Respect platform Terms of Service and API limits.
2. Prefer official APIs over brittle scraping.
3. Never store credentials in workflow JSON or repositories.
4. Require human approval for marketplace submissions and commercial commitments.
5. Deduplicate contacts and opportunities.
6. Maintain audit logs for every external action.
7. Add rate limits and stop switches.
8. Measure revenue and qualified-opportunity outcomes, not activity volume.