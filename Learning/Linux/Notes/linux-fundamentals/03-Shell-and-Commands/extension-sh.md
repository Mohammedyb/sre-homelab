# `.sh`

## Overview
The `.sh` suffix is a common filename convention for shell scripts. It does not determine which shell runs the file.

## Common Usage
```bash
bash ./health-check.sh
```
This explicitly runs the script with Bash, regardless of its filename suffix or executable bit.

## SRE Relevance
Use a clear extension and documented interpreter to improve maintainability. Validate scripts and their permissions before scheduling or deploying them.

## Quick Examples
- `bash -n health-check.sh` checks Bash syntax without running commands.
- `chmod +x health-check.sh` makes a script executable when appropriate.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `.sh` is a filename suffix, not a command with flags. |

## Related Topics
- [Bash Script](../09-Scripting-and-Automation/bash-script.md)
- [Shebang `#!`](shebang.md)
- [Permissions](../04-Users-and-Permissions/permissions.md)
