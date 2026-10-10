# -b (`journalctl` boot option)
## Overview
-b filters journal entries to a boot; use -b 0 for the current boot and -b -1 for the previous boot.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
journalctl -b -1 --no-pager
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate events into a timeline, verify recovery, and protect log access and retention.

## Quick Examples
Example: journalctl -u myapp -b 0 --no-pager

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-b 0` | Select current boot. |
| `-b -1` | Select previous boot. |
## Related Topics
[journalctl](journalctl.md), [syslog](syslog.md), [var log](var-log.md)
