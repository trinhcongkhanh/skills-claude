# <Machine / Challenge name> - Write-up

| Field | Value |
|---|---|
| Platform | HackTheBox / TryHackMe / own lab / ... |
| Difficulty | Easy / Medium / Hard |
| OS / Category | Linux / Windows / Web / Crypto / Forensics |
| Date | YYYY-MM-DD |
| Author | Trinh Cong Khanh |
| Authorization | Platform terms / own lab / written scope |

## 1. Summary
2-3 sentences: the attack path in one line (e.g. "Outdated CMS -> RCE -> sudo misconfig -> root") and the main lesson.

## 2. Recon and enumeration
Commands with short explanation of WHY each one was run and what the output means.
```bash
nmap -sC -sV -oA scans/initial 10.10.10.10
```

## 3. Initial access
Vulnerability, CVE/CWE, how it works underneath, exploitation steps.

## 4. Privilege escalation
What was found, why it is exploitable, steps.

## 5. MITRE ATT&CK mapping
| Step | Tactic | Technique (ID) |
|---|---|---|
| | | |

## 6. Detection and defense
| Step | How to detect (logs, alerts) | How to fix / harden |
|---|---|---|
| | | |

## 7. Lessons learned
- Technical:
- Methodology (what I would do faster next time):

## 8. References
- Official advisories, CVE/NVD entries, tool docs used.
