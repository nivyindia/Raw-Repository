param(
  [switch]$Install,
  [string]$Root = "$PSScriptRoot\runtime-qualification"
)

$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force -Path $Root | Out-Null

function Check-Cmd($name) {
  $c = Get-Command $name -ErrorAction SilentlyContinue
  if ($c) { Write-Host "[PASS] $name -> $($c.Source)"; return $true }
  Write-Host "[MISS] $name"; return $false
}

Write-Host "=== Nivy Reuse Runtime Qualification — Windows ==="
if (-not $Install) {
  Check-Cmd git | Out-Null
  Check-Cmd python | Out-Null
  Check-Cmd node | Out-Null
  Check-Cmd npm | Out-Null
  Check-Cmd npx | Out-Null
  Check-Cmd openclaw | Out-Null
  Check-Cmd clawhub | Out-Null
  Write-Host "Preflight only. Re-run with -Install after prerequisites are available."
  exit 0
}

if (-not (Check-Cmd python)) { throw "Python 3.11+ is required for Agent Governance Toolkit." }
if (-not (Check-Cmd node)) { throw "Node.js is required for NocoBase/MemOS integrations." }
if (-not (Check-Cmd npm)) { throw "npm is required for NocoBase." }

Write-Host ""
Write-Host "[1/4] Agent Governance Toolkit"
python -m pip install --upgrade "agent-governance-toolkit[full]"
$agt = Get-Command agt -ErrorAction SilentlyContinue
if ($agt) {
  agt doctor
  agt verify --json | Out-File -Encoding utf8 "$Root\agt-verify.json"
  Write-Host "[PASS] AGT evidence: $Root\agt-verify.json"
} else {
  Write-Warning "agt CLI not found on PATH after installation. Open a new PowerShell and run: agt doctor; agt verify --json"
}

Write-Host ""
Write-Host "[2/4] NocoBase"
npm install -g @nocobase/cli
nb --version | Tee-Object "$Root\nocobase-cli-version.txt"
$nbDir = Join-Path $Root "nocobase-test"
if (-not (Test-Path $nbDir)) {
  nb init $nbDir --ui
  Write-Host "[PASS] NocoBase test app created at $nbDir"
} else {
  Write-Host "[INFO] NocoBase test app already exists: $nbDir"
}

Write-Host ""
Write-Host "[3/4] ERPClaw"
$hasClaw = [bool](Get-Command clawhub -ErrorAction SilentlyContinue)
$hasOpenClaw = [bool](Get-Command openclaw -ErrorAction SilentlyContinue)
if ($hasClaw -and $hasOpenClaw) {
  clawhub install erpclaw
  Write-Host "[PASS] ERPClaw install attempted through OpenClaw/ClawHub."
} else {
  Write-Warning "OpenClaw/ClawHub not detected. ERPClaw runtime test is deferred."
}

Write-Host ""
Write-Host "[4/4] MemOS"
if ($hasOpenClaw) {
  $memosInstaller = Join-Path $env:TEMP "memos-install.ps1"
  Invoke-RestMethod "https://raw.githubusercontent.com/MemTensor/MemOS/main/apps/memos-local-plugin/install.ps1" -OutFile $memosInstaller
  powershell -ExecutionPolicy Bypass -File $memosInstaller
  Write-Host "[PASS] MemOS local plugin installation attempted."
} else {
  Write-Warning "OpenClaw not detected. MemOS local-plugin test is deferred."
}

Write-Host ""
Write-Host "=== Manual runtime actions still required ==="
Write-Host "ERPClaw: create company -> customer -> invoice -> payment -> report"
Write-Host "NocoBase: create data model -> workflow -> role -> AI employee -> audit event"
Write-Host "AGT: allow tool -> deny dangerous tool -> inspect audit -> verify policy"
Write-Host "MemOS: write memory -> restart/session change -> retrieve memory -> verify persistence"
Write-Host "Evidence directory: $Root"
