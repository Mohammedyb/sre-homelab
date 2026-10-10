# Octal Notation
## Overview
Octal modes encode read=4, write=2, execute=1 for owner, group, and other classes.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
chmod 640 /etc/app/app.conf
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: chmod 640 /etc/app/app.conf

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
