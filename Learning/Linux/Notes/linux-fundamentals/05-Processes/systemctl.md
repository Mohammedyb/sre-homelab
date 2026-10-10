# systemctl
## Overview
systemctl controls and queries systemd units; use service managers rather than raw signals for supervised services.

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
| `status` | Inspect unit |
| `stop/start/restart` | Change runtime state |

## Related Topics
[ps](ps.md), [top](top.md)
