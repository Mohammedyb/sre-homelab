# Stress
## Overview
Stress testing intentionally creates load to validate limits and alerts; use controlled, isolated tests rather than production hosts without approval.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
stress --cpu 2 --timeout 30s
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: stress --cpu 2 --timeout 30s

## Common Flags
| Flag | Purpose |
| --- | --- |
| `--cpu N` | Worker count |
| `--timeout` | Duration |
| `install/package availability varies` |  |

## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
