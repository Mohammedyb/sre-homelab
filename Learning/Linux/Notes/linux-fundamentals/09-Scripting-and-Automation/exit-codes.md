# Exit Codes

## Overview
An exit code (or exit status) is an integer returned by a process to its parent. By convention, `0` means success and nonzero means failure or a special condition.

## Common Usage
```bash
if grep -q 'ready' health.txt; then
  printf 'service is ready\n'
fi
```
The `if` condition checks the command's status directly without relying on printed output.

## SRE Relevance
Schedulers, CI systems, and orchestrators use exit codes to determine task success. Ensure scripts propagate failures rather than accidentally returning success after a failed command.

## Quick Examples
- `command; printf 'status=%s\n' "$?"` inspects the immediately previous command's status.
- `exit 2` explicitly ends a script with a nonzero status.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | Exit codes are process results, not command flags. |

## Related Topics
- [`$?`](dollar-question-mark.md)
- [Error Handling](error-handling.md)
- [`exit`](../03-Shell-and-Commands/exit.md)
