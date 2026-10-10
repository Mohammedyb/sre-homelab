# -eo
## Overview
ps -eo selects all processes and formats chosen columns; it is useful for scripts that need predictable fields.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ps -eo pid,ppid,user,stat,%cpu,%mem,cmd
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: ps -eo pid,ppid,user,stat,%cpu,%mem,cmd

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-e` | Select all processes. |
| `-o FIELDS` | Choose output columns. |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
