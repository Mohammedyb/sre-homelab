# -aG
## Overview
-aG with usermod appends supplementary groups without replacing existing memberships.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo usermod -aG adm appuser
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo usermod -aG adm appuser

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-a` | Append instead of replacing existing supplementary groups. |
| `-G GROUP` | Specify supplementary groups. |
## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
