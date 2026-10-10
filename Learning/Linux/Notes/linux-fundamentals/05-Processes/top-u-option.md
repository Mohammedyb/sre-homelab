# `top` User Filter (`u`)

## Overview
- In the interactive `top` monitor, press `u` to filter processes by user.
- This narrows a busy process list to workloads owned by a service account.
- The filter changes the display; it does not change process ownership or permissions.
## Common Usage
```bash
top -u api
```
Starts `top` with its user filter set to `api`.
## SRE Relevance
- Identify which account owns CPU- or memory-heavy workloads.
- Compare service-account processes during multi-tenant host incidents.
- For repeatable automation, use `ps` rather than scripting interactive `top`.
## Quick Examples
- In `top`, press `u` and enter `www-data`.
- Press `u` with an empty username to clear the filter, where supported.
- Use `ps -u api -o pid,comm,%cpu,%mem` for a one-shot report.
## Common Flags
| Flag | Description |
| --- | --- |
| `u` | Interactive `top` key that prompts for a user filter |
| `-u USER` | Start `top` filtered to a user on implementations that support it |
## Related Topics
- [`top`](top.md)
- [User-owned processes](user-owned-processes.md)
- [`ps`](ps.md)

