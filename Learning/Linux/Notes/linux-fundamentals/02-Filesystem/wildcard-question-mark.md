# `?` (Shell Glob)

## Overview
In Bash filename expansion, `?` matches exactly one character in a path component. It is not a regular expression (regex), where `?` commonly makes the previous expression optional.

## Common Usage
Use when one character varies; quote the pattern if a program such as `find` should receive it literally.

## Bash Example
```bash
printf '%s\n' file?.csv
```
Bash expands to names such as `file1.csv` and `fileA.csv`, with exactly one character in that position.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Precise patterns reduce accidental matches in batch operations. Inspect expanded results before modifying files.

## Quick Examples
- One variable character: `printf '%s\n' node?.log`
- Two variable characters: `printf '%s\n' node??.log`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `?` | A shell glob matching one character; regular-expression `?` has a different meaning. |

## Related Topics
[`*` glob](wildcard-asterisk.md), [`??` glob](wildcard-double-question-mark.md), [CSV](csv.md)
