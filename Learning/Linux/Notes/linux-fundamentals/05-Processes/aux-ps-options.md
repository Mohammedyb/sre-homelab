# aux
## Overview
In `ps aux`, `a`, `u`, and `x` are BSD-style option letters selecting broad process coverage and user-oriented output; their meanings depend on command option style.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps aux
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised graceful changes and verify recovery.

## Quick Examples
Example: ps aux

## Common Flags
| Flag | Purpose |
| --- | --- |
| `a` | Select processes for all users (BSD-style). |
| `u` | Use user-oriented output format. |
| `x` | Include processes without a controlling terminal. |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
