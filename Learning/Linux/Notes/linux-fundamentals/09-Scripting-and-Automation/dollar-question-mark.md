# `$?`

## Overview
In Bash, `$?` expands to the exit status of the most recently completed foreground command or pipeline.

## Common Usage
```bash
grep -q 'healthy' status.txt
result=$?
printf 'grep exit status: %s\n' "$result"
```
Save the value immediately: running another command changes `$?`.

## SRE Relevance
Checking status makes scripts observable and reliable. Prefer conditional syntax such as `if command; then ...` when possible to avoid accidentally overwriting the status.

## Quick Examples
- `if curl -fsS https://health.example/; then echo ok; fi` branches on the command status.
- `set -o pipefail` helps a pipeline return failure from an earlier stage.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `$?` is a shell parameter, not a command with flags. |

## Related Topics
- [Exit Codes](exit-codes.md)
- [Error Handling](error-handling.md)
- [Bash Script](bash-script.md)
