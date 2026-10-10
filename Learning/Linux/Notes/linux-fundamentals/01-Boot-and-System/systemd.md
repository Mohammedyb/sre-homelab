# systemd

## Overview
systemd is a system and service manager used as PID 1 on many Linux distributions. It manages services, sockets, mounts, timers, and targets.

## Common Usage
Inspect a production service and query its recent logs.
```bash
systemctl status ssh
journalctl -u ssh --since '1 hour ago'
```
Service names vary by distribution; verify the unit name before taking action.

## SRE Relevance
Unit dependencies, restart policies, and timers influence availability and recovery.
Use controlled reloads or restarts and confirm health after a change.

## Quick Examples
`systemctl enable --now UNIT` enables a unit at boot and starts it now; `systemctl is-active UNIT` checks runtime state.

## Common Flags
| Flag | Description |
| --- | --- |
| `systemctl --failed` | List failed units |
| `journalctl -u` | Show logs for a named unit |

## Related Topics
- [Init manager](init-manager.md)
- [D-Bus](dbus.md)
- [Application layer](application-layer.md)
