# `$`

## Overview
In Bash, `$` introduces parameter expansion, command substitution, and other expansions. Its meaning depends on the following syntax.

## Common Usage
```bash
printf 'User: %s\n' "$USER"
```
`$USER` expands to the variable value; quoting prevents word splitting and wildcard expansion.

## SRE Relevance
Quote variable expansions in scripts to avoid arguments splitting unexpectedly. Never put secrets directly into command lines where they may appear in process lists or logs.

## Quick Examples
- `"$HOME"` expands the home path as one argument.
- `"$(hostname)"` captures command output.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `$` is shell syntax whose behavior depends on the following expression. |

## Related Topics
- [Command Substitution](command-substitution.md)
- [Bash](bash.md)
- [PATH](path.md)
