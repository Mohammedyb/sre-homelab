# `rm`
## Overview
`rm` unlinks files; with recursive options it can remove directories and their contents. Removal is generally permanent and not recoverable from the command line.

## Common Usage
Inspect the exact target and glob expansion. Prefer explicit paths, backups, and previews; never use unchecked variable-expanded removals.

## Bash Example
```bash
printf 'Would remove: %s\n' ./old-output/*
```

Only previews shell expansion. Review output before adapting the command to delete anything.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Incorrect cleanup can delete production data or mounted volumes. Use scoped retention, safeguards, and approvals for destructive automation.

## Quick Examples
- Remove one confirmed file: `rm -- ./old-output.tmp`
- Preview files: `find ./cache -type f -print`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `--` | Ends option parsing so dash-leading paths are not interpreted as options. See [`-f`](rm-force-option.md) and [`-r`](recursive-option.md). |

## Related Topics
[`-f`](rm-force-option.md), [`-r`](recursive-option.md), [`rmdir`](rmdir.md), [Files](files.md)

