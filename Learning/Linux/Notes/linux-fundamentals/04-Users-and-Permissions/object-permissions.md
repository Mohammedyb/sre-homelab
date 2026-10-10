# Object Permissions
## Overview
Filesystem objects record an owner, group, and permission bits that control access.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
stat -c '%A %U:%G %n' /srv/app
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: stat -c '%A %U:%G %n' /srv/app

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
