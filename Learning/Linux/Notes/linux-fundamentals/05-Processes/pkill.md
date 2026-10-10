# pkill
## Overview
pkill sends a signal to processes matching a pattern and can target user or full command; avoid broad matches.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
pkill -TERM -u appuser worker
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: pkill -TERM -u appuser worker

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-f` | Match full command |
| `-u` | Match user |
| `-x` | Exact name |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
