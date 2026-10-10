# CSV (Comma-Separated Values)
## Overview
Comma-separated values (CSV) is a plain-text tabular format. Quoting and escaping mean commas and newlines can occur inside fields, so splitting every line on commas is unsafe.

## Common Usage
Use a CSV-aware parser for transformations. For command-line inspection, preserve the source and verify headers, encoding, and record counts.

## Bash Example
```bash
head -n 5 -- metrics.csv; file -- metrics.csv
```

Previews initial lines and identifies file type; this is not a full CSV validation.

## SRE Relevance
Site reliability engineering (SRE) teams should note: CSV carries exports, metrics, and inventory. Validate schema and protect sensitive fields before sharing or ingestion.

## Quick Examples
- Count physical lines: `wc -l < metrics.csv`
- Find CSV files: `find . -type f -name '*.csv' -print`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `head -n 5` | Limits display to five lines; line count may differ from CSV records if quoted fields span lines. |

## Related Topics
[`ls *.csv`](ls-csv-glob.md), [`*` glob](wildcard-asterisk.md), [Files](files.md)

