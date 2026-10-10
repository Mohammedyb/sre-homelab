# su
## Overview
su starts a shell or command as another user; it commonly requests that user's password, unlike sudo policy checks.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
su - appuser
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: su - appuser

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
