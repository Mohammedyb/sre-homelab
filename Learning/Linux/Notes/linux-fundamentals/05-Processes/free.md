# `free`

## Overview
- `free` reports physical memory and swap usage.
- It reads kernel memory statistics and provides a point-in-time summary.
- Linux uses otherwise-unused memory for cache, so inspect the `available` value when assessing pressure.
## Common Usage
```bash
free -h
```
Displays memory totals in human-readable units.
## SRE Relevance
- Check memory pressure during latency, out-of-memory, or swap incidents.
- Use `watch` or monitoring systems for trends; a single snapshot can miss spikes.
- Correlate host memory with container limits and per-process usage.
## Quick Examples
- `free -h` - readable summary.
- `free -w` - separate cache and buffers where supported.
- `watch -n 2 free -h` - refresh the summary every two seconds.
## Common Flags
| Flag | Description |
| --- | --- |
| `-h` | Human-readable units |
| `-w` | Wide output with cache and buffers separated |
| `-s N` | Repeat the report every N seconds |
## Related Topics
- [Memory health metrics](memory-health-metrics.md)
- [Swap memory](swap-memory.md)
- [`vmstat`](vmstat.md)

