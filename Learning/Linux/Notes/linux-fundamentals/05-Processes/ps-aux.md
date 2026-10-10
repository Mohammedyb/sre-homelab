# `ps aux`

## Overview
- `ps aux` lists processes with user-oriented columns using BSD-style option letters.
- `a` selects processes for all users, `u` formats user details, and `x` includes processes without a terminal.
## Common Usage
```bash
ps aux --sort=-%cpu | head
```
Shows the highest-CPU processes first; use `ps -eo` for explicit output columns.
## SRE Relevance
- Identify resource-heavy processes and their owners during host incidents.
- Treat this as a snapshot; use monitoring or `top` to observe changing resource use.
- Avoid killing a process based only on its name; verify its PID and service first.
## Quick Examples
- `ps aux --sort=-%mem | head` lists memory-heavy processes.
- `ps -u api -o pid,stat,etime,cmd` inspects one service account's processes.
## Common Flags
| Option | Description |
| --- | --- |
| `a` | Include processes associated with terminals across users |
| `u` | Show user-oriented columns |
| `x` | Include processes without a controlling terminal |
## Related Topics
- [`ps`](ps.md)
- [`top`](top.md)
- [`kill`](kill.md)
