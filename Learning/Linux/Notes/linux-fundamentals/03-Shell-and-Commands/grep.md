# Grep

## Overview
`grep` searches input for lines matching a pattern. It supports regular expressions and can read files or standard input.

## Common Usage
```bash
grep -n 'timeout' /var/log/app.log
```
This prints matching lines with line numbers; quote patterns to prevent shell expansion.

## SRE Relevance
Use targeted patterns and bounded log ranges to keep incident output useful. Treat logs as untrusted data and avoid dumping credentials or personal information.

## Quick Examples
- `grep -i 'error' app.log` ignores case.
- `grep -E '5[0-9][0-9]' access.log` matches common HTTP 5xx status codes.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-i` | Ignore case. |
| `-n` | Show line numbers. |
| `-v` | Select nonmatching lines; see [`-v`](grep-v.md). |
| `-r` | Search directories recursively. |

## Related Topics
- [`-v` (grep option)](grep-v.md)
- [Pipe Character `|`](pipe-character.md)
- [Tail](tail.md)
