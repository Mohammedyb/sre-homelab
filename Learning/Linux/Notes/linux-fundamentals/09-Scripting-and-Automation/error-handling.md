# Error Handling

## Overview
Error handling detects failures, reports useful context, and exits or recovers deliberately. Bash scripts can inspect statuses and use traps for cleanup.

## Common Usage
```bash
if ! curl -fsS --max-time 5 https://health.example/; then
  printf 'health check failed\n' >&2
  exit 1
fi
```
The request has a timeout, errors are reported to stderr, and the script returns a failure status.

## SRE Relevance
Good failure handling prevents silent partial deployments and supports alerting. Make retries bounded, operations idempotent where possible, and diagnostics safe for logs.

## Quick Examples
- `set -euo pipefail` enables common Bash safeguards; understand their edge cases.
- `trap 'rm -f "$tmpfile"' EXIT` can clean a known temporary file on exit.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | Error handling is a scripting practice; commands and shells provide their own options. |

## Related Topics
- [Exit Codes](exit-codes.md)
- [`$?`](dollar-question-mark.md)
- [Standard Error](../03-Shell-and-Commands/standard-error-stderr.md)
