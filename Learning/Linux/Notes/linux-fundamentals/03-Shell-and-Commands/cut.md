# Cut

## Overview
`cut` extracts selected bytes, characters, or delimiter-separated fields from each input line.

## Common Usage
```bash
cut -d: -f1 /etc/passwd
```
This prints the first colon-delimited field, typically usernames.

## SRE Relevance
Use `cut` for simple, well-formed delimited text. It does not correctly parse general CSV quoting; choose a CSV-aware tool for complex data.

## Quick Examples
- `cut -c1-12 file.txt` selects columns by character position.
- `cut -d, -f2 report.csv` selects a comma-separated field if values contain no quoted commas.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-d CHAR` | Set the field delimiter. |
| `-f LIST` | Select fields. |
| `-c LIST` | Select character positions. |

## Related Topics
- [Sort](sort.md)
- [CSV](../02-Filesystem/csv.md)
- [Pipe Character `|`](pipe-character.md)
