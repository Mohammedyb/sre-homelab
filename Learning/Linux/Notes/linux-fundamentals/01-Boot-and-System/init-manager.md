# Init Manager

## Overview
An init manager is the first user-space process started by the kernel and coordinates system initialization.
It starts services, manages dependencies, and handles shutdown; systemd is a widely used init manager.

## Common Usage
Check the process with process identifier (PID) 1 and identify the init implementation.
```bash
ps -p 1 -o pid,comm,args
readlink -f /sbin/init
```
This is useful when service-management commands differ between container or host environments.

## SRE Relevance
Init behavior determines service ordering, restart policy, and shutdown handling.
Understand whether a workload runs on a full host or a container with a different PID 1.

## Quick Examples
On systemd hosts, `systemctl` manages units; minimal containers may use a purpose-built init process.

## Common Flags
| Flag | Description |
| --- | --- |
| `ps -p` | Select a process by PID |
| `readlink -f` | Resolve a symlink to its canonical path |

## Related Topics
- [systemd](systemd.md)
- [D-Bus](dbus.md)
