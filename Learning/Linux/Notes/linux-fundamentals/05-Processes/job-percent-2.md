# %2
## Overview
%2 is a shell job specifier for job number 2, not a process ID; use jobs to confirm its current mapping.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
fg %2
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: fg %2

## Common Flags
| Flag | Purpose |
| --- | --- |
| `%N` | Refer to shell job N |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
