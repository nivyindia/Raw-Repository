# Revenue workflow set

Four executable n8n workflow definitions are provided:

1. `revenue-01-lead-intake-to-scoring.json` — A036 → A037 → A039
2. `revenue-02-outreach.json` — A043 → A049 → A044
3. `revenue-03-reply-qualification.json` — A052 → A054
4. `revenue-04-meeting-proposal-onboarding.json` — A055 → A060 → A065

Set `AIOS_RUNTIME_URL` in the n8n environment. Import the JSON files into n8n and connect credentials/providers through n8n's credential system.

The workflows intentionally return drafts/routing results rather than silently sending messages. A044 remains approval-gated according to the AIOS agent contract.
