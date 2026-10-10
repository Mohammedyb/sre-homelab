# logger
## Overview
logger submits a test message to the system logging service, useful for checking local routing and collection.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
logger -t deploy-check -p user.err 'synthetic test event'
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate events into a timeline, verify recovery, and protect log access and retention.

## Quick Examples
Example: journalctl -t deploy-check --since '5 minutes ago'

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-t TAG` | Set the message tag. |
| `-p FACILITY.SEVERITY` | Set syslog priority. |
## Related Topics
[journalctl](journalctl.md), [syslog](syslog.md), [var log](var-log.md)
