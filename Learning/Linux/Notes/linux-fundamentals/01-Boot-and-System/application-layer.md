# Application Layer

## Overview
The application layer is user-space software above the kernel and system libraries; examples include web servers, databases, monitoring agents, and command-line tools.

## Common Usage
Inspect a service's process and logs when an application is unhealthy.
```bash
systemctl status nginx
journalctl -u nginx --since '15 minutes ago'
```
Replace `nginx` with the affected production service to correlate state with recent errors.

## SRE Relevance
Application availability depends on its configuration, dependencies, and host resources as well as the kernel.
Monitor service health and validate a rollback path before deploying changes.

## Quick Examples
Use `curl -fS http://127.0.0.1/health` for a local HTTP health check when the application exposes one.

## Common Flags
| Flag | Description |
| --- | --- |
| `systemctl status` | Show unit state and recent status details |
| `journalctl -u` | Filter journal entries by systemd unit |

## Related Topics
- [Kernel](kernel.md)
- [Init manager](init-manager.md)
- [systemd](systemd.md)
