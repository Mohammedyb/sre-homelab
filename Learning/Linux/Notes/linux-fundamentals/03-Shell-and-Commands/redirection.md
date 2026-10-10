# `>` (redirection)

## Overview
The `>` shell operator redirects a command's standard output to a file, creating or truncating that file before execution.

## Common Usage
```bash
printf '%s\n' 'check complete' > check.txt
```
This replaces the contents of `check.txt`; confirm the target path before using `>`.

## SRE Relevance
Redirection can destroy existing data immediately. Use a temporary, reviewed destination for generated output and avoid truncating production files by mistake.

## Quick Examples
- `command > output.log` writes stdout to a file.
- `command 2> error.log` redirects stderr separately.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `>` is shell syntax, not a command with flags. |

## Related Topics
- [`>>` (append redirection)](append-redirection.md)
- [Standard Output](standard-output-stdout.md)
- [`1` (stdout file descriptor)](fd-1-stdout.md)
