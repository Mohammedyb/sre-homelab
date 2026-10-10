# `locate`
## Overview
`locate` finds paths by querying a prebuilt filename database, often faster than traversing the filesystem. Results may be stale, missing, or restricted.

## Common Usage
Treat hits as leads; confirm with `stat` or `test -e`. Use `find` when freshness or live filesystem predicates matter.

## Bash Example
```bash
locate -i 'nginx.conf' | head
```

Searches the database case-insensitively and shows a small sample.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Fast inventory helps incident response, but stale indexes can mislead automation. Confirm the live file and respect access policy.

## Quick Examples
- Search exact path pattern: `locate '/etc/nginx/nginx.conf'`
- Refresh where permitted: `sudo updatedb`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-i` | Ignores case. Implementation and database access vary; see [`updatedb`](updatedb.md). |

## Related Topics
[`find`](find.md), [`updatedb`](updatedb.md), [Absolute path](absolute-path.md)

