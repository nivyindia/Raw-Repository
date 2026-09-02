# Founder + Backup Admin 2FA/SSO Checklist — Billion Dreams United AIOS

**Version:** 1.0  
**Control ID:** IAM-FOUNDER-ADMIN-001  
**Stage:** D.9  
**Status:** Required before production go-live

## 1. Objective

Establish a resilient two-person privileged-access control: one Founder administrator and one designated Backup Administrator, without relying on shared credentials.

## 2. Identity Rules

- [ ] Founder has a unique named account.
- [ ] Backup Administrator has a unique named account.
- [ ] Shared administrator accounts are prohibited.
- [ ] Both identities use the minimum privileges required for their role.
- [ ] Backup Administrator is operationally independent enough to recover access if the Founder is unavailable.
- [ ] Recovery contact details are stored securely and reviewed periodically.

## 3. MFA / 2FA Baseline

For Founder and Backup Administrator:

- [ ] MFA/2FA enabled on the primary identity provider.
- [ ] MFA/2FA enabled on GitHub.
- [ ] MFA/2FA enabled on Vaultwarden.
- [ ] MFA/2FA enabled on infrastructure/admin consoles.
- [ ] MFA/2FA enabled on Odoo administration.
- [ ] MFA/2FA enabled on other systems holding production credentials or sensitive business data.
- [ ] Prefer phishing-resistant authentication (FIDO2/WebAuthn/security key) where supported.
- [ ] At least one hardware/security-key recovery method is registered for each privileged administrator where supported.
- [ ] Recovery codes are generated and stored offline in an approved secure location.
- [ ] Recovery codes are never stored in Git, tickets, chat, email, or plain-text notes.

## 4. SSO Baseline

Where an identity provider/SSO layer is deployed:

- [ ] SSO is enabled for supported internal applications.
- [ ] Founder and Backup Administrator are assigned through named groups/roles rather than shared accounts.
- [ ] Privileged roles require MFA.
- [ ] SSO session duration follows the organization's security policy.
- [ ] Inactive or terminated users are removed from privileged groups promptly.
- [ ] Break-glass access is separate from normal SSO identities and tightly controlled.
- [ ] SSO configuration changes require an auditable administrative action.

## 5. Break-Glass / Recovery

- [ ] A documented emergency-access procedure exists.
- [ ] Break-glass credentials are not used for routine administration.
- [ ] Break-glass credentials are stored in the approved secure secret-management system.
- [ ] Access to break-glass credentials is limited to authorized administrators.
- [ ] Every break-glass use is logged with reason, operator, time, scope, and outcome.
- [ ] Break-glass credentials are rotated after use or suspected exposure.
- [ ] Recovery procedure is tested periodically without exposing production secrets.

## 6. GitHub Privileged Access

- [ ] Founder account has MFA enabled.
- [ ] Backup Administrator account has MFA enabled.
- [ ] Organization/repository admin rights are granted only where necessary.
- [ ] Production deployment rights are separated from ordinary contributor rights where practical.
- [ ] Branch protection/rulesets require appropriate review for protected production branches.
- [ ] Personal access tokens are minimized and scoped narrowly.
- [ ] SSH keys/tokens are individually attributable and rotatable.
- [ ] Secrets are stored in approved secret stores, never committed to repositories.

## 7. Vaultwarden Privileged Access

- [ ] Founder has a named Vaultwarden account with MFA.
- [ ] Backup Administrator has a named Vaultwarden account with MFA.
- [ ] DEV/STAGING/PROD vault/collection access is separated.
- [ ] PROD secrets are inaccessible to ordinary development identities.
- [ ] Vaultwarden emergency/recovery mechanism is documented.
- [ ] Critical recovery information is securely escrowed according to company policy.
- [ ] Access review is performed at least quarterly and after role changes.

## 8. Administrative Separation

Founder and Backup Administrator must not approve their own exceptional access when separation of duties is required.

For material actions:

`Request → Policy Evaluation → Approval → Execution → Audit`

For L3/L4 actions, applicable AIOS approval and human-review requirements remain mandatory; administrator status does not bypass them.

## 9. Recovery Test

At least periodically, verify that the Backup Administrator can independently:

- [ ] authenticate with MFA;
- [ ] access required recovery documentation;
- [ ] retrieve authorized recovery secrets;
- [ ] restore access to critical systems;
- [ ] revoke a compromised credential;
- [ ] rotate affected credentials;
- [ ] verify system access after recovery;
- [ ] produce an audit record of the exercise.

## 10. Incident Response

If a privileged account is compromised or suspected compromised:

1. Revoke active sessions/tokens where possible.
2. Disable or restrict the affected identity if required.
3. Rotate exposed credentials and recovery secrets.
4. Check audit logs for unauthorized activity.
5. Notify the other authorized administrator.
6. Preserve relevant evidence.
7. Restore access using the documented recovery path.
8. Record the incident and corrective actions.

## 11. Review Cadence

| Control | Review |
|---|---|
| Founder MFA | Monthly verification / after security event |
| Backup Admin MFA | Monthly verification / after security event |
| Privileged access assignments | Monthly |
| Recovery codes / recovery material | Quarterly and after use |
| Break-glass procedure | Quarterly |
| Recovery test | Quarterly |
| SSO configuration | Quarterly and after material change |
| GitHub privileged access | Monthly |
| Vaultwarden privileged access | Monthly |

## 12. Evidence

Maintain evidence without exposing secrets:

- MFA enrollment/status evidence
- SSO group/role assignment evidence
- privileged-access review records
- recovery-test record
- break-glass access log
- credential rotation/revocation record
- security incident references

Never place passwords, MFA seeds, recovery codes, API tokens, private keys, or other secret values in this checklist.

## 13. Completion Gate

D.9 is complete only when:

- Founder and Backup Administrator identities are uniquely assigned;
- MFA/2FA is enabled on all critical privileged systems;
- SSO is configured where applicable;
- recovery material is securely stored;
- break-glass procedure exists;
- recovery test has passed;
- evidence is recorded without exposing secrets.

## 14. Cross-References

- `07-policies/permission-matrix.yaml`
- `07-policies/ai-risk-policy.yaml`
- `07-policies/communication-policy.yaml`
- `07-policies/suppression-list-data-model.yaml`
- `07-policies/iam-baseline.md`
- `07-policies/approval-workflow-spec.md`
