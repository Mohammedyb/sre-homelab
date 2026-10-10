# Command Substitution

## Overview
Command substitution captures a command's standard output and inserts it into another command. Bash supports both `$(...)` and legacy backticks.

## Common Usage
```bash
backup="backup-$(date -u '+%F').tar"
```
The date output becomes part of the assigned filename; quoting preserves spaces if output contains them.

## SRE Relevance
Use `$(...)` for readable automation and quote substitutions when passing values as arguments. Command substitution removes trailing newline characters.

## Quick Examples
- `host=$(hostname)` stores command output in a variable.
- `printf 'Host: %s\n' "$(hostname)"` passes it safely as one argument.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | Command substitution is shell syntax, not a command with flags. |

## Related Topics
- [`$`](dollar-sign.md)
- [Date](date.md)
- [Bash Script](../09-Scripting-and-Automation/bash-script.md)
