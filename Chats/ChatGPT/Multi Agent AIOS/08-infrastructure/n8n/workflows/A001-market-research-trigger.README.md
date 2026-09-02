# A001 n8n Trigger Integration

## Purpose

Connect the registered A001 Market Research Agent to an n8n event boundary for F.1.3.

## Trigger contract

- Method: `POST`
- Path: `/webhook/aios/a001/market-research`
- Required input: `research_question`, `target_market`
- Optional input: `geography`, `industry`, `customer_segment`, `time_horizon`, `competitor_set`, `source_policy`, `output_format`
- Event type default: `market.research.requested`
- Agent: `A001`

## Execution boundary

The workflow validates and normalizes the incoming event, then passes it to the registered A001 runtime boundary. The workflow does **not** fabricate an agent execution result.

A real F.1.3 completion requires:

1. Import/enable this workflow in the AIOS n8n instance.
2. Connect the `A001 Runtime Boundary` node to the actual registered agent executor (LangGraph/AIOS runtime).
3. Send one real `market.research.requested` event.
4. Capture the execution ID and resulting `research.completed` event.
5. Record the evidence in the A001 status/test log.

Until steps 1–4 are executed against a live runtime, F.1.3 must not be marked as 60%.
