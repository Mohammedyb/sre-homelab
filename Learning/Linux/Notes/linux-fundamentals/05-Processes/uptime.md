# `uptime`

## Overview
- `uptime` reports the current time, duration since boot, logged-in user count, and load averages.
- Load averages summarize runnable and uninterruptible tasks over 1, 5, and 15 minutes.
- It is a fast first check, not a direct measure of CPU utilization.
## Common Usage
```bash
uptime
```
Compare load averages with CPU count and follow up with process and resource tools.
## SRE Relevance
- Establish whether a host recently rebooted during incident triage.
- Spot sustained load growth and correlate it with CPU, I/O, and workload metrics.
- Monitor trends rather than alerting on one sample alone.
## Quick Examples
- `uptime` - show load averages and boot duration.
- `uptime -p` - show boot duration in a friendly format.
- `uptime -s` - show the system boot time.
## Common Flags
| Flag | Description |
| --- | --- |
| `-p` | Display uptime in a human-friendly format |
| `-s` | Display the date and time the system started |
## Related Topics
- [Load average](load-average.md)
- [CPU health metrics](cpu-health-metrics.md)
- [`top`](top.md)

