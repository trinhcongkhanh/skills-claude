---
name: secure-code-and-lab
description: Use when writing or reviewing code, designing or querying databases, doing security reviews, or working on cyber security labs, CTFs and authorized pentests - coding standards, SQL safety, OWASP/CWE checks, lab workflow and write-ups mapped to MITRE ATT&CK.
---

# Secure code and lab

Three parts. Use the part that fits the task; security review (Part C) applies to all code.

---
## Part A - Code standards (any language)

**Naming and structure**
- Names say intent: `failed_login_count`, not `x` or `data2`. Python snake_case, JS/TS camelCase, classes PascalCase, constants UPPER_SNAKE.
- One function = one job; aim for under ~40 lines. Early return instead of deep nesting.
- Group by feature, keep config separate from code, no magic numbers (name them).

**Comments and docs**
- Comment the *why*, not the *what*. Every public function: purpose, params, return, errors raised.
- README for every project: what it does, how to run, how to test, security notes.

**Errors and logging**
- Catch specific exceptions; never `except: pass`.
- Log events (auth failures, permission denials, input rejected) with timestamp and context; NEVER log passwords, tokens, full card numbers or personal data.
- Show users generic error messages; keep stack traces in logs only.

**Secrets and dependencies**
- No secrets in code or git. Use environment variables or a secret manager (AWS Secrets Manager, SSM Parameter Store, Vault). Add `.env` to `.gitignore`; scan with `gitleaks` or `trufflehog` before pushing.
- Pin dependency versions; run `pip-audit` / `npm audit` / Dependabot.

**Tests**
- At least: one happy path, one edge case (empty, max size, unicode), one malicious input per input handler.
- Run the code before saying it works.

---
## Part B - Databases

1. **Always parameterized queries** - never build SQL with string concatenation or f-strings.
```python
# BAD - SQL injection (CWE-89)
cur.execute(f"SELECT * FROM users WHERE email = '{email}'")

# GOOD - parameterized (psycopg / sqlite3 style placeholders)
cur.execute("SELECT id, email FROM users WHERE email = %s", (email,))
```
2. **Least privilege** - app account gets only the needed `SELECT/INSERT/UPDATE` on its schema; no `DROP`, no superuser, separate read-only account for reporting.
3. **Select only needed columns** - avoid `SELECT *` (performance and accidental data exposure).
4. **Indexes** - index columns used in `WHERE`, `JOIN`, `ORDER BY`; confirm with `EXPLAIN` / `EXPLAIN ANALYZE`; remember each index slows writes.
5. **Transactions** - wrap multi-step changes (e.g. payment + order) in a transaction; choose the isolation level deliberately.
6. **Passwords** - store with a slow hash: Argon2id (preferred) or bcrypt; never MD5/SHA1/plain SHA-256.
7. **Sensitive data** - encrypt at rest, mask in logs and non-prod copies, define retention.
8. **Migrations** - versioned scripts (Alembic, Flyway, Prisma Migrate); never edit prod schema by hand; back up and test restore.
9. **NoSQL** - still validate types; block operator injection (e.g. a `{"$ne": null}` object where a string was expected in MongoDB).

---
## Part C - Security review checklist (map findings to CWE)
| Check | Common weakness |
|---|---|
| All input validated server-side (type, length, allow-list) | CWE-20 |
| SQL / NoSQL parameterized | CWE-89 |
| Output encoded for its context (HTML, JS, URL) | CWE-79 (XSS) |
| No user input reaching shell / `eval` | CWE-78, CWE-94 |
| File paths normalized and restricted | CWE-22 |
| Every endpoint checks authorization, not just authentication | CWE-862, CWE-639 (IDOR) |
| State-changing requests protected (SameSite cookies, CSRF token) | CWE-352 |
| Server-side URL fetch restricted (allow-list, block metadata IPs like 169.254.169.254) | CWE-918 (SSRF) |
| No hardcoded credentials | CWE-798 |
| No unsafe deserialization of untrusted data (pickle, Java native) | CWE-502 |
| Security headers / TLS / cookie flags (HttpOnly, Secure, SameSite) | CWE-614, CWE-1004 |

Group findings under the OWASP Top 10:2025 categories (final edition Jan 2026; verify at owasp.org/Top10). For web/app/extension specifics use the `app-build-standards` skill if installed. Report each finding as: title, severity (CVSS rating), location, impact, proof (in lab), fix, reference.

---
## Part D - Cyber lab / CTF / authorized pentest workflow

**0. Scope check (mandatory)**
Proceed only if the target is: the user's own lab (VMs, home lab, cloud account they own), a CTF / training platform (HackTheBox, TryHackMe, PortSwigger Academy, picoCTF, DVWA, Juice Shop), or covered by written authorization. If unclear, ask. Never help attack real third-party systems, and say so briefly.

**1. Environment** - Kali Linux or similar in an isolated network (host-only / NAT, snapshots before risky steps). Keep a notes file from minute one.

**2. Phases** (with ATT&CK tactic IDs for the write-up)
| Phase | Typical actions (lab) | ATT&CK tactic |
|---|---|---|
| Recon | passive info, `nmap -sC -sV -oA scan target` | Reconnaissance TA0043, Discovery TA0007 |
| Enumeration | web dirs, SMB shares, versions -> search known CVEs | Discovery TA0007 |
| Initial access | exploit the vuln found, default creds | Initial Access TA0001, Execution TA0002 |
| Privilege escalation | SUID, sudo rules, kernel/service misconfig | Privilege Escalation TA0004 |
| Credential access / lateral | hash dumping, reuse (lab only) | Credential Access TA0006, Lateral Movement TA0008 |
| Persistence (only if the lab asks) | | Persistence TA0003 |
| Cleanup | remove shells, accounts, files you created | - |

Always pair each offensive step with the defensive view: what log/alert would catch it (Windows Event IDs, Sysmon, auditd, IDS rules), and the fix/hardening (patch, config, CIS Benchmark item).

**3. Write-up** - use `references/writeup-template.md`. Apply the `cyber-dark-style` skill (light mode) if it is installed. Good write-ups are portfolio material for a CV: explain the reasoning, not just commands; redact flags only if the platform requires it.
