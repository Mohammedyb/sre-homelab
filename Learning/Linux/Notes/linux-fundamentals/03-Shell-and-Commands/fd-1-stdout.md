# `1` (stdout file descriptor)

## Overview
File descriptor `1` is the conventional descriptor for standard output (stdout), where a process writes normal results.

## Common Usage
```bash
printf '%s\n' 'ok' 1> status.txt
```
`1>` explicitly redirects stdout; simple `>` is equivalent in the shell.

## SRE Relevance
Explicit stdout redirection helps keep command output organized for jobs and diagnostic capture. Know whether an output file will be created or overwritten.

## Quick Examples
- `command > result.txt` is shorthand for `1>`.
- `command 1>&2` sends stdout to stderr.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `1` is a file descriptor, not a command option. |

## Related Topics
- [Standard Output](standard-output-stdout.md)
- [`2` (stderr file descriptor)](fd-2-stderr.md)
- [`>` (redirection)](redirection.md)
