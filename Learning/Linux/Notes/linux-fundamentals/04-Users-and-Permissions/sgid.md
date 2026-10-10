# Set Group ID (SGID)
## Overview
SGID on an executable runs it with the file's group identity; on directories it causes group inheritance.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
find /srv -type d -perm -2000 -ls
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: find /srv -type d -perm -2000 -ls

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
