# Syslog
## Overview
Syslog is a logging protocol and family of services for routing and storing event messages from hosts and applications.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
logger -p user.err 'deployment check failed'
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate events into a timeline, verify recovery, and protect log access and retention.

## Quick Examples
Example: sudo tail -n 50 /var/log/syslog

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[journalctl](journalctl.md), [var log](var-log.md)
