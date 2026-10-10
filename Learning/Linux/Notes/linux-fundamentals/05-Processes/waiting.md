# Waiting
## Overview
Waiting is a broad condition for a process blocked on an event; D often denotes uninterruptible kernel sleep such as I/O wait.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -eo pid,stat,wchan:24,comm
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -eo pid,stat,wchan:24,comm

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-o stat,wchan` | Include state and kernel wait channel |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
