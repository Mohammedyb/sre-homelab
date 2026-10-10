# Zombie
## Overview
A zombie (Z) has exited but its parent has not yet collected its exit status; it holds a process-table entry, not active CPU or memory.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -eo pid,ppid,stat,cmd | awk '$3
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -eo pid,ppid,stat,cmd | awk '$3

## Common Flags
| Flag | Purpose |
| --- | --- |
| `ps -o pid,ppid,stat,cmd -p 1234` |  |
, ## Related Topics, , [ampersand](ampersand.md)

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
