# Set User ID (SUID)
## Overview
SUID on an executable runs it with the file owner's effective identity, often root; it is a sensitive privilege boundary.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
find /usr -xdev -type f -perm -4000 -ls
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: find /usr -xdev -type f -perm -4000 -ls

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
