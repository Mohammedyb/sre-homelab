# `Ctrl+C`

## Overview
`Ctrl+C` sends the interrupt signal (usually SIGINT) to the foreground process group in a terminal. Programs may handle, ignore, or act on the signal.

## Common Usage
```bash
sleep 60
```
Press `Ctrl+C` while it runs to interrupt it; the shell then returns to the prompt.

## SRE Relevance
Interrupt a hanging foreground diagnostic safely, but know whether the command has already changed data. For managed services, use the service manager rather than terminal interrupts.

## Quick Examples
- Press `Ctrl+C` to stop `tail -f` or an interactive `watch`.
- `kill -INT PID` sends SIGINT to a selected process after confirming its identity.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `Ctrl+C` is a terminal key sequence, not a command with flags. |

## Related Topics
- [Bash Script](bash-script.md)
- [Exit Codes](exit-codes.md)
- [Watch](../03-Shell-and-Commands/watch.md)
