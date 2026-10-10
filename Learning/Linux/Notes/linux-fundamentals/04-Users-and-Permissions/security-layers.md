# Security Layers
## Overview
Linux access checks include identity, discretionary permissions, access control lists, capabilities, and mandatory security policy.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
id; namei -l /srv/app/data
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: id; namei -l /srv/app/data

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
