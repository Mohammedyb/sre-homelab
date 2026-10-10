# Standard Input (stdin)

## Overview
Standard input (stdin) is the default input stream read by a process. It is commonly connected to the keyboard or to another command through a pipe.

## Common Usage
```bash
printf '%s\n' 'check' | wc -c
```
The pipe connects `printf` output to `wc` standard input.

## SRE Relevance
Pipelines let tools process data without intermediate files. Ensure commands consume expected input and do not block waiting for an interactive prompt in automation.

## Quick Examples
- `command < input.txt` redirects a file to stdin.
- `read -r answer` reads one line from stdin in Bash.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | stdin is a process stream, not a command with flags. |

## Related Topics
- [Standard Output](standard-output-stdout.md)
- [Pipe Character `|`](pipe-character.md)
- [`0` (stdin file descriptor)](fd-0-stdin.md)
