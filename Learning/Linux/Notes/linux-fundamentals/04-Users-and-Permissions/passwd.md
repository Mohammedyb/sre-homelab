# Sudo Passwd
## Overview
passwd changes or manages an account password; sudo passwd USER administers another account's local password.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo passwd appuser
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo passwd appuser

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
