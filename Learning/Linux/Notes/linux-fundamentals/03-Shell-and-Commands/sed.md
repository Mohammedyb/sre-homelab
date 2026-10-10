# Sed

## Overview
`sed` is a stream editor for transforming text line by line. It can select, replace, or delete text without opening an interactive editor.

## Common Usage
```bash
sed 's/ERROR/WARN/' app.log
```
This writes transformed output to standard output and leaves the source file unchanged.

## SRE Relevance
Preview edits before changing configuration in place. In-place syntax differs across GNU and BSD `sed`; keep backups and validate configuration after changes.

## Quick Examples
- `sed -n '1,20p' file` prints lines 1 through 20.
- `sed 's/old/new/g' file` replaces all occurrences on each line in output.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-n` | Suppress default printing; combine with explicit print commands. |
| `-E` | Use extended regular expressions on common implementations. |
| `-i` | Edit files in place; syntax varies by platform. |

## Related Topics
- [`s/`](sed-substitution.md)
- [Grep](grep.md)
- [Standard Output](standard-output-stdout.md)
