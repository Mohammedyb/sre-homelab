# `kill -9`
## Overview
- `kill -9 PID` sends signal 9 (`SIGKILL`) to a process.
- The kernel terminates the process immediately; it cannot catch the signal or clean up.
- Prefer a normal termination request first, because forced termination can leave work incomplete.
## Common Usage
```bash
kill -TERM 1234
sleep 5
kill -KILL 1234
```
Allow time for graceful shutdown before escalating to `SIGKILL` if the process remains.
## SRE Relevance
- Forced termination can interrupt writes or leave temporary state behind.
- Confirm the PID and service owner before escalation in production.
- For managed services, use the service manager and inspect logs after termination.
## Quick Examples
- `kill -KILL 1234` - force termination as a last resort.
## Common Flags
| Flag | Description |
| --- | --- |
| `-9` | Numeric form of `SIGKILL`; immediate forced termination |
| `-KILL` | Named form of `SIGKILL` |
| `-TERM` | Named form of the default graceful termination signal |
## Related Topics
- [`kill`](kill.md)
- [SIGTERM](sigterm.md)
- [SIGKILL](sigkill.md)
- [Process termination](process-termination.md)
