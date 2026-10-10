# Standard Error (stderr)

## Overview
Standard error (stderr) is the conventional stream for diagnostics and error messages. It is separate from standard output.

## Common Usage
```bash
command >result.txt 2>errors.txt
```
The shell saves normal output and diagnostics to separate files; replace `command` with the intended safe operation.

## SRE Relevance
Capturing stderr separately helps diagnose failed jobs without mixing diagnostics into machine-readable output. Avoid discarding errors with `2>/dev/null` unless they are intentionally irrelevant.

## Quick Examples
- `tool 2>&1` combines stderr with stdout.
- `tool 2>error.log` redirects only error output.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | stderr is a process stream, not a command with flags. |

## Related Topics
- [Standard Output](standard-output-stdout.md)
- [`2` (stderr file descriptor)](fd-2-stderr.md)
- [Error Handling](../09-Scripting-and-Automation/error-handling.md)
