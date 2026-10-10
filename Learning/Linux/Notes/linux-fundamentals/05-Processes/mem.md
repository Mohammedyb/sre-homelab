# Mem
## Overview
Mem is a common shortened label for physical memory metrics; distinguish used, available, cache, and reclaimable memory.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
free -h
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: free -h

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-h` | Human-readable output |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
