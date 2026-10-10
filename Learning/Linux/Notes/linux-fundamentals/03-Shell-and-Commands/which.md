# `which`

## Overview
`which` reports the executable path selected by searching directories in `PATH`. It may be an external program or a shell-specific function.

## Common Usage
```bash
which curl
```
This commonly prints the path to the `curl` executable, or nothing if it cannot be found.

## SRE Relevance
Check command resolution after package installs and in deployment environments. For Bash built-ins and aliases, use `type` because `which` may not show them.

## Quick Examples
- `which ssh` checks whether SSH is on the current path.
- `type -a curl` lists all Bash resolutions, including multiple binaries.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `which` flags differ across implementations; `type` is often more portable in shells. |

## Related Topics
- [Which Command](which-command.md)
- [`PATH`](path.md)
- [Binary](binary.md)
