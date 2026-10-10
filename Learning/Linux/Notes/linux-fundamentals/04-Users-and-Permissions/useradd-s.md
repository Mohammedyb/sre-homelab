# -s (`useradd` shell option)
## Overview
-s selects the account login shell; service identities commonly use a non-login shell where appropriate.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo useradd -m -s /usr/sbin/nologin metrics-agent
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo useradd -m -s /usr/sbin/nologin metrics-agent

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-s SHELL` | Select the login shell. |
## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
