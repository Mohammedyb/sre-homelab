# SIGQUIT
## Overview
SIGQUIT asks a process to quit and typically produces a core dump; unlike SIGTERM, applications may not handle it gracefully.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
kill -QUIT 1234
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: kill -QUIT 1234

## Common Flags
| Flag | Purpose |
| --- | --- |
| `QUIT` | Signal name for SIGQUIT |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
