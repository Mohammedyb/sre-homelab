# usermod
## Overview
usermod modifies account properties such as groups, shell, home, and expiry.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo usermod -aG deployers appuser
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo usermod -aG deployers appuser

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-aG GROUP` | Append supplementary groups without replacing existing groups. |
| `-s SHELL` | Set the login shell. |
## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
