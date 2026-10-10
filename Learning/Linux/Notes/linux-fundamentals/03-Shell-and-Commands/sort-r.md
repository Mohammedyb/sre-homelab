# `-r` (sort reverse option)

## Overview
The `-r` option reverses the ordering produced by `sort`. The comparison method still depends on other options and locale.

## Common Usage
```bash
sort -nr response-times.txt
```
The combined options sort numeric values from highest to lowest.

## SRE Relevance
Reverse numeric sorting can surface highest latency or resource values first. Ensure the data is parsed as numbers, not strings.

## Quick Examples
- `sort -r names.txt` prints reverse lexicographic order.
- `sort -t, -k3,3nr report.csv` orders a third comma-delimited field numerically in reverse.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-r` | Reverse the sort order. |
| `-n` | Use numeric comparison when combined with `-r`. |

## Related Topics
- [Sort](sort.md)
- [`-k` (sort key option)](sort-k.md)
- [CSV](../02-Filesystem/csv.md)
