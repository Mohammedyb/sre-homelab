# Wc

## Overview
`wc` counts lines, words, bytes, or characters in files or standard input. The name means word count.

## Common Usage
```bash
wc -l /var/log/app.log
```
This reports the line count, useful for checking log volume or input size.

## SRE Relevance
Counts can quickly detect unexpected output growth or empty files. Byte counts and character counts differ for multibyte text.

## Quick Examples
- `wc -c artifact.tar` reports bytes.
- `grep -i error app.log | wc -l` counts matching lines.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-l` | Count lines. |
| `-w` | Count words. |
| `-c` | Count bytes. |
| `-m` | Count characters. |

## Related Topics
- [Grep](grep.md)
- [Pipe Character `|`](pipe-character.md)
- [Head](head.md)
