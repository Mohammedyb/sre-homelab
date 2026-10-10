# systemctl status
## Overview
systemctl status displays unit state, recent logs, and process information useful for initial service triage.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
systemctl status myapp
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: systemctl status myapp

## Common Flags
| Flag | Purpose |
| --- | --- |
| `--no-pager` | Print without opening an interactive pager. |
| `-l` | Do not truncate status output. |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
