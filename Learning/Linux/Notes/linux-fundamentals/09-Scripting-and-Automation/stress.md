# Stress

## Overview
`stress` is a workload generator that can consume CPU, memory, or other resources for testing. It is not generally installed by default.

## Common Usage
```bash
stress --cpu 1 --timeout 10s
```
This requests one CPU worker for ten seconds; run only on a disposable or explicitly approved test system.

## SRE Relevance
Controlled load tests validate monitoring and capacity assumptions, but unrestricted stress can cause outages or data loss. Define limits, get authorization, and watch resource saturation.

## Quick Examples
- Check `stress --help` for options supported by the installed version.
- Prefer isolated test environments and short durations; stop safely if impact exceeds the plan.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `--cpu N` | Start N CPU workers. |
| `--vm N` | Start N virtual-memory workers; can exhaust memory. |
| `--timeout DURATION` | Stop after a duration on versions that support it. |

## Related Topics
- [Yes](yes.md)
- [Watch](../03-Shell-and-Commands/watch.md)
- [Error Handling](error-handling.md)
