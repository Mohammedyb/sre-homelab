# `2` (stderr file descriptor)

## Overview
File descriptor `2` is the conventional descriptor for standard error (stderr), where a process writes diagnostic messages.

## Common Usage
```bash
command 2> errors.log
```
The shell redirects stderr to `errors.log`; replace `command` with the operation being run.

## SRE Relevance
Preserving stderr helps explain failed automation. Redirect streams deliberately and be aware that redirection order changes what is captured.

## Quick Examples
- `command 2>&1` sends stderr to the current stdout destination.
- `command >out.log 2>err.log` keeps streams separate.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `2` is a file descriptor, not a command option. |

## Related Topics
- [Standard Error](standard-error-stderr.md)
- [`1` (stdout file descriptor)](fd-1-stdout.md)
- [`>` (redirection)](redirection.md)
