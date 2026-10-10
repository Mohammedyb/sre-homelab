# killall
## Overview
killall signals processes by command name; implementations differ, so confirm platform behavior and match scope.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
killall -TERM worker
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: killall -TERM worker

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-s` | Signal |
| `-u` | User |
| `avoid broad or ambiguous names` |  |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
