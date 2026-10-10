# `s/`

## Overview
In `sed`, the `s/old/new/` command substitutes matching text. The slash is a delimiter and can be replaced with another character.

## Common Usage
```bash
sed 's/timeout=30/timeout=60/' app.conf
```
This prints a changed version to standard output; it does not update the file unless an in-place option is used.

## SRE Relevance
Always review generated configuration before deployment. Match specific values and test the resulting file to prevent broad or unintended replacements.

## Quick Examples
- `sed 's/error/ERROR/g' log.txt` replaces all matches per line.
- `sed 's|/old/path|/new/path|g' file` uses `|` as delimiter for paths.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `g` | Replace every match on each line, instead of only the first. |
| `-i` | Apply changes in place; behavior and backup syntax vary. |

## Related Topics
- [Sed](sed.md)
- [Grep](grep.md)
- [`/etc`](../02-Filesystem/etc-directory.md)
