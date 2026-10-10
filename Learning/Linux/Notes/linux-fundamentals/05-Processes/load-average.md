# Load Average
## Overview
Load average reflects average runnable and uninterruptible tasks over 1, 5, and 15 minutes; compare with CPU count and I/O pressure.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
uptime
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: uptime

## Common Flags
| Flag | Purpose |
| --- | --- |
| `N/A` | No command-specific flags apply. |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
