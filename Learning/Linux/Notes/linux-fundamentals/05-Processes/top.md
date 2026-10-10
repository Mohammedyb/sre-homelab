# top
## Overview
top interactively refreshes process and system resource metrics; use batch mode for automated snapshots.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
top
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: top

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-b` | Batch mode. |
| `-n N` | Number of iterations. |
| `-p PID` | Monitor a process ID. |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md)
