# Terminated Processes

## Overview
- A process is terminated after it exits or receives a signal that ends it.
- Its parent collects the exit status; until then, an exited child may briefly appear as a zombie.
- A terminated process is no longer consuming CPU, though its logs and exit status may explain a failure.
## Common Usage
```bash
ps -p 1234 -o pid,stat,etime,cmd
```
If the process is absent, inspect its service manager and logs to determine why it exited.
## SRE Relevance
- Unexpected exits can indicate crashes, failed health checks, deploy issues, or out-of-memory kills.
- Check service restart counts and exit status during incident response.
- Alert on repeated restarts or failed jobs rather than every expected short-lived process exit.
## Quick Examples
- `systemctl status api.service` - inspect a service's current and recent state.
- `journalctl -u api.service -b` - review service logs from this boot.
## Common Flags
| Flag | Description |
| --- | --- |
| `-p PID` | With `ps`, inspect a specific process ID |
| `-o FORMAT` | Select process fields to display |
| `-b` | With `journalctl`, limit logs to the current boot |
## Related Topics
- [Process termination](process-termination.md)
- [Zombie processes](zombie.md)
- [`systemctl`](systemctl.md)
- [`journalctl`](../06-Logging-and-Monitoring/journalctl.md)
