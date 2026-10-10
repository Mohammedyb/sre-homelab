# Sort

## Overview
`sort` orders lines of text. By default, it compares lines lexicographically according to locale settings.

## Common Usage
```bash
sort -u hosts.txt
```
This sorts lines and emits each distinct line once; validate locale-sensitive ordering when results must be reproducible.

## SRE Relevance
Sorting makes reports and comparisons easier, but sorting is not necessarily numeric or chronological by default. Set `LC_ALL=C` for deterministic bytewise sorting when appropriate.

## Quick Examples
- `sort -n latency.txt` sorts numeric values.
- `sort -r names.txt` reverses the sort order.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-n` | Compare numerically. |
| `-r` | Reverse the result order; see [`-r`](sort-r.md). |
| `-k` | Sort by a selected key/field; see [`-k`](sort-k.md). |
| `-u` | Output only unique lines. |

## Related Topics
- [`-r` (sort reverse option)](sort-r.md)
- [`-k` (sort key option)](sort-k.md)
- [Cut](cut.md)
