# `-v` (grep option)

## Overview
The `-v` option makes `grep` select lines that do not match the pattern. This is called inverse matching.

## Common Usage
```bash
grep -v '^#' app.conf
```
This excludes lines beginning with `#`; blank lines are still included.

## SRE Relevance
Inverse matching can remove comments or known noise from diagnostic output. Confirm the filter does not hide relevant failures before relying on it.

## Quick Examples
- `grep -v '^$' file` removes empty lines.
- `grep -v -e '^#' -e '^$' file` excludes comments and blank lines.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-v` | Print lines that do not match. |

## Related Topics
- [Grep](grep.md)
- [Pipe Character `|`](pipe-character.md)
- [Sed](sed.md)
