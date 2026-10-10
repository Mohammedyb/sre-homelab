# vmstat
## Overview
vmstat reports process, memory, swap, I/O, system, and CPU statistics; the first row often averages since boot.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
vmstat 1 5
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: vmstat 1 5

## Common Flags
| Flag | Purpose |
| --- | --- |
| `1` | Sampling interval |
| `5` | Number of samples |
| `-w` | Wide output |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
