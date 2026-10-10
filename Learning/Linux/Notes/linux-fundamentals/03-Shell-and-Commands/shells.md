# Shells

## Overview
A shell reads commands, expands variables and patterns, and starts programs. Common shells include Bash, Zsh, and Dash.

## Common Usage
```bash
printf 'Shell process: %s\n' "$SHELL"
```
`$SHELL` usually names the configured login shell; `$0` can indicate the current script or shell invocation.

## SRE Relevance
Scripts can behave differently under different shells. Declare the intended interpreter and test with that shell rather than assuming interactive-shell settings.

## Quick Examples
- `bash --version` checks the Bash version.
- `ps -p "$$" -o comm=` inspects the current shell process on common Linux systems.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | Each shell has its own options. |

## Related Topics
- [Bash](bash.md)
- [Bash Script](../09-Scripting-and-Automation/bash-script.md)
- [Shebang `#!`](shebang.md)
