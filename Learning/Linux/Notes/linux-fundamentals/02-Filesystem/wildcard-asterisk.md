# `*` (Shell Glob)

## Overview
In Bash filename expansion, `*` matches zero or more characters in one path component, usually excluding leading-dot names. It is a shell glob, not a regular expression (regex).

## Common Usage
Quote patterns when passing them to tools like `find` so they receive the pattern literally. Preview expansion before destructive commands.

## Bash Example
```bash
printf '%s\n' ./*.csv
```
Bash expands `*.csv` in the current directory before `printf`; with default settings, an unmatched pattern remains unchanged.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Globs may match many files or none. Validate expansions and handle empty matches deliberately in Bash scripts.

## Quick Examples
- Match all visible names: `printf '%s\n' *`
- Hidden files require deliberate shell options or explicit patterns.

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `*` | Shell pattern matching zero or more characters; differs from regular expression `.*`. |

## Related Topics
[`?` glob](wildcard-question-mark.md), [`??` glob](wildcard-double-question-mark.md), [CSV](csv.md)
