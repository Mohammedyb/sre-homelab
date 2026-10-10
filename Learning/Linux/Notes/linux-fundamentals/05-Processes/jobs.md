# Jobs
## Overview
jobs lists background and stopped jobs belonging to the current shell; it does not list arbitrary system processes.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
jobs -l
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: jobs -l

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-l` | Include process IDs |
| `-p` | List process IDs only |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
