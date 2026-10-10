# `df`

## Overview
- `df` reports available and used space on mounted filesystems.
- It helps identify full disks and exhausted container or host volumes.
- It reports filesystem capacity, unlike `du`, which summarizes directory usage.
## Common Usage
```bash
df -hT
```
Shows mounted filesystem types and capacity in human-readable units.
## SRE Relevance
- Disk exhaustion can prevent logging, deployments, and database writes.
- Check capacity during incidents and monitor important mount points.
- Use `df -i` when writes fail despite available space to check inode exhaustion.
## Quick Examples
- `df -h /var` - check the filesystem containing `/var`.
- `df -ih` - inspect inode usage.
- `df -hT` - include filesystem type.
## Common Flags
| Flag | Description |
| --- | --- |
| `-h` | Human-readable sizes |
| `-T` | Include filesystem type |
| `-i` | Report inode usage instead of block usage |
## Related Topics
- [Memory health metrics](memory-health-metrics.md)
- [System logs](../06-Logging-and-Monitoring/system-logs.md)
- [`/var`](../02-Filesystem/var-directory.md)

