# Memory Health Metrics
## Overview
Memory health includes available memory, reclaim, page faults, swap activity, and out-of-memory events.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
free -h; vmstat 1 5
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: free -h; vmstat 1 5

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-h` | Human-readable sizes (free) |
| `interval and count (vmstat)` |  |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
