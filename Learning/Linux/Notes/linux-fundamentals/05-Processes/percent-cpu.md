# -%cpu
## Overview
-%cpu is the descending CPU sort key in GNU ps syntax when passed as --sort=-%cpu; it is not a standalone option.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -eo pid,comm,%cpu --sort=-%cpu | head
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -eo pid,comm,%cpu --sort=-%cpu | head

## Common Flags
| Flag | Purpose |
| --- | --- |
| `--sort=-%cpu` | Sort with highest CPU usage first (GNU ps). |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
