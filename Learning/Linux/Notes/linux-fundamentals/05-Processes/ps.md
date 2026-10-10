# ps
## Overview
ps snapshots processes; select useful fields and filter by PID or user to investigate resource use and parentage.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -eo pid,ppid,user,stat,%cpu,%mem,cmd
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -eo pid,ppid,user,stat,%cpu,%mem,cmd

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-e` | Select all processes. |
| `-o` | Specify output fields. |
| `-p PID` | Select process ID. |
## Related Topics
[systemctl](systemctl.md), [top](top.md)
