# SIGTERM
## Overview
SIGTERM requests graceful shutdown and lets an application flush data or clean up if it handles the signal.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
kill -TERM 1234
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: kill -TERM 1234

## Common Flags
| Flag | Purpose |
| --- | --- |
| `TERM` | Default signal for kill |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
