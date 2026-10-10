# `-k` (sort key option)

## Overview
The `-k` option selects one or more fields as the sort key. Field numbering and separators should be chosen explicitly for structured text.

## Common Usage
```bash
sort -t, -k2,2 report.csv
```
This sorts comma-separated rows by the second field; standard `sort` is not a full CSV parser when fields contain quoted commas.

## SRE Relevance
Sorting metrics by a specific column helps prioritize investigation. Validate delimiters and header handling to avoid misleading rankings.

## Quick Examples
- `sort -k2,2n metrics.txt` sorts the second whitespace-delimited field numerically.
- `sort -t: -k3,3n /etc/passwd` orders by numeric third field.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-k KEYDEF` | Select the field or character range used for sorting. |
| `-t CHAR` | Set the field delimiter. |
| `-n` | Compare the key numerically. |

## Related Topics
- [Sort](sort.md)
- [`-r` (sort reverse option)](sort-r.md)
- [Cut](cut.md)
