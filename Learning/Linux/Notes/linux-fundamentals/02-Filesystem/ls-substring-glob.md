# `ls *csv*`
## Overview
The Bash glob `*csv*` matches names containing lowercase `csv` anywhere in one path component. It can match multiple extensions and is case-sensitive by default.

## Common Usage
Preview broad matches before acting; substring globs can include unrelated files. Use an explicit directory and constrained suffix when possible.

## Bash Example
```bash
printf '%s\n' -- *csv*
```

Prints names in the current directory containing `csv`; it does not recursively search subdirectories.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Broad globs can include unintended artifacts in cleanup or upload jobs. Prefer constrained patterns and explicit directories.

## Quick Examples
- CSV suffix only: `printf '%s\n' ./*.csv`
- Inspect types: `file -- *csv*`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `*csv*` | Shell pattern with leading and trailing `*`, each matching zero or more characters; not an `ls` flag. |

## Related Topics
[`ls *.csv`](ls-csv-glob.md), [`*` glob](wildcard-asterisk.md), [CSV](csv.md)

