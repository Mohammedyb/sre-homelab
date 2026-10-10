# -p (`ps`/`pstree` PID option)
## Overview
The -p option is command-specific: ps -p selects process IDs, while pstree -p displays PID annotations.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -p 1234 -o pid,ppid,cmd
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -p 1234 -o pid,ppid,cmd

## Common Flags
| Flag | Purpose |
| --- | --- |
| `ps -p PID` | Select a process by PID. |
| `pstree -p` | Display PIDs in the process tree. |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
