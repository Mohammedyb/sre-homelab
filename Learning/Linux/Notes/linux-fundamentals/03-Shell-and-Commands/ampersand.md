# `&`

## Overview
In shell syntax, a trailing `&` starts a command asynchronously in the background. It does not automatically manage output, cleanup, or service lifecycle.

## Common Usage
```bash
long-running-check >check.log 2>&1 &
```
The shell returns a job identifier; the output is captured, and the process may end when the session closes.

## SRE Relevance
For durable workloads use a service manager, scheduler, or orchestrator rather than a terminal background job. Track and stop temporary jobs deliberately.

## Quick Examples
- `sleep 30 &` starts a short background process.
- `jobs` lists jobs in the current shell; `wait` waits for one.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `&` is shell control syntax, not a command with flags. |

## Related Topics
- [Bash](bash.md)
- [Standard Output](standard-output-stdout.md)
- [Exit Codes](../09-Scripting-and-Automation/exit-codes.md)
