# 2 Complains
## Overview
Octal digit 2 means write only; “Complains” is a mnemonic, not a Linux permission term.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
chmod 620 /srv/app/queue
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: chmod 620 /srv/app/queue

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
