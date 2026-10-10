# --disk-usage
## Overview
journalctl --disk-usage reports disk space used by archived and active journal files.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
journalctl --disk-usage
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate events into a timeline, verify recovery, and protect log access and retention.

## Quick Examples
Example: sudo journalctl --vacuum-time=14d

## Common Flags
| Flag | Purpose |
| --- | --- |
| `--disk-usage` | Report disk used by journal files. |
| `--vacuum-time=TIME` | Remove archived entries older than a duration. |
## Related Topics
[journalctl](journalctl.md), [syslog](syslog.md), [var log](var-log.md)
