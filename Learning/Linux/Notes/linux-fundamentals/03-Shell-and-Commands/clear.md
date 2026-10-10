# `clear`

## Overview
`clear` clears the visible terminal display. It does not delete shell history, logs, or files.

## Common Usage
```bash
clear
```
This resets the visible screen so recent output is easier to inspect.

## SRE Relevance
Clearing a terminal can reduce visual clutter during incident response, but it removes context from view. Capture needed output before clearing.

## Quick Examples
- Press `Ctrl+L` in many shells to clear the display.
- `clear; pwd` clears the screen and then prints the current directory.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | Behavior is terminal-dependent; `clear` has no portable standard flags. |

## Related Topics
- [Terminal](terminal.md)
- [Bash](bash.md)
- [Command Line](command-line.md)
