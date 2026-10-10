# -p (`logger` priority option)
## Overview
-p selects the syslog facility and severity for a message, such as user.err or daemon.warning.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
logger -p user.err 'synthetic test event'
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate events into a timeline, verify recovery, and protect log access and retention.

## Quick Examples
Example: logger -p daemon.warning -t healthcheck 'latency high'

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-p PRIORITY` | Set facility and severity, for example `user.err`. |
## Related Topics
[journalctl](journalctl.md), [syslog](syslog.md), [var log](var-log.md)
