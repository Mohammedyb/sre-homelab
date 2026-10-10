# SIGKILL
## Overview
SIGKILL forcibly terminates a process and cannot be caught or ignored; it prevents cleanup and should be a last resort.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
kill -KILL 1234
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: kill -KILL 1234

## Common Flags
| Flag | Purpose |
| --- | --- |
| `KILL` | Signal name for SIGKILL |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
