# Standard Output (stdout)

## Overview
Standard output (stdout) is the default stream where a process writes normal results. It is usually displayed in the terminal unless redirected.

## Common Usage
```bash
printf '%s\n' 'deployment ready' > status.txt
```
The shell redirects stdout to `status.txt`, replacing its existing contents.

## SRE Relevance
Separate normal output from errors so automation can process results and diagnostics independently. Protect output files from unintended overwrite.

## Quick Examples
- `command > output.txt` redirects stdout.
- `command | grep ready` sends stdout to another command's stdin.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | stdout is a process stream, not a command with flags. |

## Related Topics
- [Standard Error](standard-error-stderr.md)
- [Pipe Character `|`](pipe-character.md)
- [`1` (stdout file descriptor)](fd-1-stdout.md)
