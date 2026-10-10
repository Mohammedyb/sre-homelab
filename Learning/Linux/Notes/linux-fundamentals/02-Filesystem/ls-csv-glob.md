# `ls *.csv`
## Overview
Bash expands `*.csv` to matching names in the current directory before `ls` runs. It matches names ending `.csv` and usually excludes hidden files.

## Common Usage
Use `printf` or null-delimited loops in scripts rather than parsing human-oriented `ls` output. Quote paths and use `--` for dash-leading names.

## Bash Example
```bash
printf '%s\n' -- ./*.csv
```

Previews CSV-like names through shell expansion; unmatched behavior depends on shell options.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Data-file batches feed pipelines. Check whether a glob matched and handle whitespace and newlines safely in automation.

## Quick Examples
- Interactive listing: `ls -- *.csv`
- Bash array: `files=(./*.csv); printf '%s\n' "${files[@]}"`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `*.csv`, `--` | A filename glob, not an `ls` option; `--` ends `ls` option parsing. See [`ls`](../03-Shell-and-Commands/ls.md). |

## Related Topics
[CSV](csv.md), [`*` glob](wildcard-asterisk.md), [`ls *csv*`](ls-substring-glob.md)

