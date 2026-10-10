# `cat`

## Overview
`cat` reads files and writes their contents to standard output. Its name comes from concatenation; it can combine multiple inputs.

## Common Usage
```bash
cat /etc/hostname
```
This displays a small configuration value; use a pager for large files.

## SRE Relevance
Use `cat` for short text, not huge logs or binary files. Protect secrets in configuration files and avoid exposing them in recorded terminal output.

## Quick Examples
- `cat first.txt second.txt` prints files in order.
- `cat -- file.txt` treats a leading-hyphen filename as a path.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-n` | Number all output lines. |
| `-A` | Show nonprinting characters on many implementations. |

## Related Topics
- [Less](less.md)
- [Head](head.md)
- [Standard Output](standard-output-stdout.md)
