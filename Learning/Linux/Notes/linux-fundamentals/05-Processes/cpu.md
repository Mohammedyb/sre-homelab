# CPU
## Overview
CPU is the central processing unit; Linux CPU metrics include user, system, idle, I/O wait, and steal time.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
top
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: top

## Common Flags
| Flag | Purpose |
| --- | --- |
| `1` | Sample interval in seconds |
| `count limits samples` |  |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
