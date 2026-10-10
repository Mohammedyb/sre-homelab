# /etc/passwd
## Overview
The /etc/passwd file maps local names to user IDs (UIDs), primary group IDs (GIDs), home directories, and login shells; modern password hashes are stored elsewhere.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
getent passwd appuser
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: getent passwd appuser

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
