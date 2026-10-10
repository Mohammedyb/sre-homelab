# `-n` (echo option)

## Overview
For many `echo` implementations, `-n` suppresses the newline normally printed after the text. Its behavior is not fully portable.

## Common Usage
```bash
printf 'healthy'
```
Use `printf` instead of relying on `echo -n` when exact output matters; this example emits no newline.

## SRE Relevance
Missing newlines can make logs or command output run together. For scripts, prefer `printf` for predictable output and explicit formatting.

## Quick Examples
- `echo -n "token:"` writes a prompt without a line break (implementation-dependent).
- `printf '%s' "token:"` is the portable alternative; do not print actual credentials.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-n` | Suppress the trailing newline in many shells and implementations. |

## Related Topics
- [`echo`](echo.md)
- [Standard Output](standard-output-stdout.md)
- [Bash](bash.md)
