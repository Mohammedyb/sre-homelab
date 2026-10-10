# `exit`

## Overview
`exit` ends the current shell or script and may provide an exit status. An exit status of `0` conventionally means success; nonzero indicates a problem.

## Common Usage
```bash
exit 1
```
This terminates the current shell or script with status `1`; use care in interactive sessions.

## SRE Relevance
Schedulers and monitoring use exit status to decide whether automation succeeded. Avoid accidentally ending an SSH session while working on a host.

## Quick Examples
- `exit 0` reports success.
- `exit` without an argument uses the last command's status in Bash.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `exit` accepts an optional numeric status, not standard flags. |

## Related Topics
- [Exit Codes](../09-Scripting-and-Automation/exit-codes.md)
- [`$?`](../09-Scripting-and-Automation/dollar-question-mark.md)
- [Bash](bash.md)
