# --sort
## Overview
GNU ps --sort orders process output by a selected field; a leading minus sorts descending.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps aux --sort=-%cpu | head
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps aux --sort=-%cpu | head

## Common Flags
| Flag | Purpose |
| --- | --- |
| `--sort=FIELD` | Sort by a process field; prefix `-` for descending. |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
