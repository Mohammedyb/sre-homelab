# Running
## Overview
Running (R) means a process is executing or runnable and waiting for CPU time.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -eo pid,stat,comm | awk '$2
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -eo pid,stat,comm | awk '

## Common Flags
| Flag | Purpose |
| --- | --- |
| `top` |  |
, ## Related Topics, , [ampersand](ampersand.md)

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
