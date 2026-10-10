# Process Startup
## Overview
Process startup creates a process from a program and environment; systemd services, shells, and parent processes are common launch paths.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
systemctl show -p ExecStart,MainPID myapp
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: systemctl show -p ExecStart,MainPID myapp

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-p` | Select process ID |
| `--user` | Inspect user services |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
