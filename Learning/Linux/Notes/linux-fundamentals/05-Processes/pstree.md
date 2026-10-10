# pstree
## Overview
pstree visualizes parent-child process relationships, helping identify who launched a process.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
pstree -p 1
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: pstree -p 1

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-p` | Display process IDs. |
| `-a` | Show command arguments. |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
