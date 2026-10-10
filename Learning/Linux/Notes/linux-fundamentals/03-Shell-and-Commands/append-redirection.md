# `>>` (append redirection)

## Overview
The `>>` shell operator redirects standard output to a file and appends data instead of truncating existing contents.

## Common Usage
```bash
printf '%s\n' 'check complete' >> check.log
```
This adds a line to the end of `check.log`, creating the file if needed.

## SRE Relevance
Appending preserves prior output but can still grow a file without limit. Use log rotation or managed logging for ongoing production logs.

## Quick Examples
- `command >> output.log` appends stdout.
- `command 2>> error.log` appends stderr to a separate file.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `>>` is shell syntax, not a command with flags. |

## Related Topics
- [`>` (redirection)](redirection.md)
- [Standard Output](standard-output-stdout.md)
- [Syslog](../06-Logging-and-Monitoring/syslog.md)
