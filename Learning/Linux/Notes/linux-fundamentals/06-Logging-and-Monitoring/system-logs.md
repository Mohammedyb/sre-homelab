# System Logs
## Overview
System logs record kernel, service, authentication, and application events; location and format depend on distribution and logging configuration.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
journalctl -p warning -b --no-pager
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate events into a timeline, verify recovery, and protect log access and retention.

## Quick Examples
Example: journalctl -u nginx --since '1 hour ago' --no-pager

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[journalctl](journalctl.md), [syslog](syslog.md), [var log](var-log.md)
