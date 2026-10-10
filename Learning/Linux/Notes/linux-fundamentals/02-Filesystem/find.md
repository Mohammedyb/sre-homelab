# `find`
## Overview
`find` searches a directory hierarchy with predicates such as name, type, time, and size. It can also perform actions, so preview matches first.

## Common Usage
Start narrowly and quote patterns so `find`, not the shell, interprets them. Use `-print` for safe preview.

## Bash Example
```bash
find /var/log -type f -name '*.log' -print
```

Prints regular files under `/var/log` with names ending `.log`.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Useful for inventory and retention investigations. Bound searches on large filesystems and review results before destructive `-exec` actions.

## Quick Examples
- Files over 100 MB: `find /var -xdev -type f -size +100M -print`
- See the [`-type` predicate](find-type.md).

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-type`, `-name`, `-xdev` | Selects file kinds, matches names, and avoids crossing filesystem boundaries. `-name` uses a pattern interpreted by `find`. |

## Related Topics
[`-type`](find-type.md), [`locate`](locate.md), [`updatedb`](updatedb.md), [Directories](directories.md)

