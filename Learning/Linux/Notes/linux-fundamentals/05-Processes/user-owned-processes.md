# User-Owned Processes
## Overview
User-owned processes run for interactive sessions or applications under a non-root identity.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -u appuser -o pid,ppid,stat,cmd
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -u appuser -o pid,ppid,stat,cmd

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-u USER` | Filter by user |
| `-o` | Select output fields |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
