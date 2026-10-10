# System-Owned Processes
## Overview
System-owned processes run under service identities or root to provide host functions; inspect their executable and service unit before acting.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -eo pid,user,comm --sort=user | head
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -eo pid,user,comm --sort=user | head

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-u USER` | Filter by owner (ps) |
| `system services are distribution-specific` |  |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
