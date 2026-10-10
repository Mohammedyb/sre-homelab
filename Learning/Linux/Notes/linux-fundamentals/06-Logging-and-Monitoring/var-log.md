# Var/Log
## Overview
/var/log is a common directory for persistent text logs, though modern distributions may store events in systemd-journald instead.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo ls -lah /var/log
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate events into a timeline, verify recovery, and protect log access and retention.

## Quick Examples
Example: sudo tail -n 100 /var/log/syslog

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[journalctl](journalctl.md), [syslog](syslog.md)
