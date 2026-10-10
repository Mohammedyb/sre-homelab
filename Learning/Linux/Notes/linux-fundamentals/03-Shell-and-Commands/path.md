# `PATH`

## Overview
`PATH` is an environment variable containing colon-separated directories where a shell searches for executable commands.

## Common Usage
```bash
printf '%s\n' "$PATH"
```
This prints the current search path, one string; inspect it before changing command resolution.

## SRE Relevance
Different `PATH` values in login shells, services, and CI jobs can select different tool versions or make commands unavailable. Avoid adding untrusted writable directories.

## Quick Examples
- `command -v curl` checks how the shell resolves a command.
- `export PATH="/opt/tools/bin:$PATH"` prepends a trusted directory for this shell and child processes.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `PATH` is a variable, not a command with flags. |

## Related Topics
- [Which Command](which-command.md)
- [`which`](which.md)
- [Command substitution](command-substitution.md)
