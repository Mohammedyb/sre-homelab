# Stopped
## Overview
Stopped (T) means a process was suspended by job control or a stop signal and is not currently scheduled to run.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -o pid,stat,cmd -p 1234
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -o pid,stat,cmd -p 1234

## Common Flags
| Flag | Purpose |
| --- | --- |
| `N/A` | No command-specific flags apply. |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
