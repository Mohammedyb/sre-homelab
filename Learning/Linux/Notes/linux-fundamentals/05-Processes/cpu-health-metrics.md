# CPU Health Metrics
## Overview
CPU health is assessed from utilization, runnable work, saturation, and throttling over a time window, not one sample alone.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
uptime; vmstat 1 5
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: uptime; vmstat 1 5

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-` | Sample interval for vmstat |
| `1` | seconds |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
