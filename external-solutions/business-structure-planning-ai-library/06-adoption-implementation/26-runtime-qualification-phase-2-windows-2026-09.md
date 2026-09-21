# Runtime Qualification — Windows — Phase 2

## Purpose

This package moves qualification from source inspection to local runtime testing.

The GitHub tools cannot execute software on the user's Windows PC, so this script prepares and runs the install/verification steps when the user executes it locally.

## Run

Preflight:

powershell -ExecutionPolicy Bypass -File .\RUN-PHASE-2-WINDOWS.ps1

Install and qualification setup:

powershell -ExecutionPolicy Bypass -File .\RUN-PHASE-2-WINDOWS.ps1 -Install

## Test matrix

| Candidate | Runtime test | Evidence |
|---|---|---|
| ERPClaw | company → customer → invoice → payment → report | records/logs |
| NocoBase | data model → workflow → role → AI employee → audit | app/log/export evidence |
| Agent Governance Toolkit | allow → deny → audit → verification | agt verify + audit output |
| MemOS | write → restart/session change → retrieve | persistence evidence |

## Official runtime facts used

ERPClaw currently documents ClawHub installation and OpenClaw as its primary runtime.

NocoBase currently documents installation through its CLI:

npm install -g @nocobase/cli
nb init --ui

Microsoft Agent Governance Toolkit currently documents:

pip install "agent-governance-toolkit[full]"
agt doctor
agt verify

MemOS currently documents a Windows PowerShell local-plugin installer and requires an installed supported agent runtime such as OpenClaw, Hermes, or DeepSeek Harness.

## Important

The script intentionally does not mark a candidate as adopted. Runtime evidence must pass before an adapter is implemented.
