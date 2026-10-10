# kill -l
## Overview
kill -l lists signal names and numbers supported by the running system.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
kill -l
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: kill -l

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-l` | List signal names supported on this host. |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
