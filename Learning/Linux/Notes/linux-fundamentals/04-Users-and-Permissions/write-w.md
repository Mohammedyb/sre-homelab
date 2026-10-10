# Write (w)
## Overview
The write bit permits changing a file; on directories it permits creating or removing entries when execute is also allowed.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
test -w /var/lib/app
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: test -w /var/lib/app

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
