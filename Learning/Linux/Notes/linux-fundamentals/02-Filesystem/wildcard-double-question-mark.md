# `??` (Bash Glob)

## Overview
In Bash, `??` is two `?` glob operators and matches exactly two characters in that pathname component. It is not a special regular-expression (regex) token: `??` is generally a lazy optional quantifier on the previous token in engines that support it.

## Common Usage
Use for fixed-width patterns; leading dots normally need explicit matching. Bash recursive `**` requires `globstar` and is unrelated.

## Bash Example
```bash
printf '%s\n' host??.csv
```
Matches names such as `host01.csv`; one or three characters after `host` do not match.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Fixed-width patterns can select shard or node names, but validate matches before batch changes and account for shell options.

## Quick Examples
- Two-character suffix: `printf '%s\n' shard??.log`
- Regular-expression exact pair example: `^host..\.csv$`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `??` | Two shell wildcards, each matching one character. Regular expressions have different rules; do not transfer glob patterns unchanged. |

## Related Topics
[`?` glob](wildcard-question-mark.md), [`*` glob](wildcard-asterisk.md), [`find`](find.md)
