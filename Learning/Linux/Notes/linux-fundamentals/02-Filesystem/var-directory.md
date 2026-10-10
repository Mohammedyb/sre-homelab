# Var (`/var`)
## Overview
`/var` stores data that changes during operation, such as logs, caches, queues, and service state. Contents vary by workload.

## Common Usage
Monitor `/var` capacity: a full filesystem can disrupt logging, package operations, and services. Identify owners before cleanup.

## Bash Example
```bash
du -sh /var/log /var/cache 2>/dev/null; df -h /var
```

Summarizes common variable-data directories and checks the filesystem containing `/var`.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Capacity alerts prevent outages. Use service-aware cleanup and retention policies instead of deleting unknown state.

## Quick Examples
- Summarize immediate entries: `du -xhd1 /var 2>/dev/null`
- Inspect logs in [`/var/log`](var-log.md).

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `du -x`, `df -h` | `du -x` stays on one filesystem; `-h` formats sizes for people. |

## Related Topics
[`/var/log`](var-log.md), [Files](files.md), [Directories](directories.md)

