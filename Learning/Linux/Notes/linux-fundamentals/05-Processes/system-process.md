# System Process
## Overview
A system process performs operating-system or infrastructure work, often as a daemon or kernel thread.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -eo pid,ppid,user,stat,comm --sort=pid | head
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -eo pid,ppid,user,stat,comm --sort=pid | head

## Common Flags
| Flag | Purpose |
| --- | --- |
| `N/A` | No command-specific flags apply. |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
