# Var/Log (`/var/log`)
## Overview
`/var/log` commonly holds system and service log files, though journald and distribution conventions vary. Logs are records, not the logging system itself.

## Common Usage
Read with `less`, `tail`, or `journalctl`; use rotation and retention policies instead of deleting active logs manually.

## Bash Example
```bash
tail -n 50 /var/log/syslog 2>/dev/null || journalctl -n 50 --no-pager
```

Shows recent file-based logs when present, otherwise recent system-journal entries.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Logs support incident diagnosis and audit. Collection, observability, and logging concepts are cross-linked to the [Logging category](../06-Logging-and-Monitoring/var-log.md).

## Quick Examples
- Follow a file: `tail -F /var/log/syslog`
- Query a service: `journalctl -u nginx --since '1 hour ago'`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `tail -F`, `journalctl --no-pager` | Follows across rotation; disables interactive paging for scripts. |

## Related Topics
[Logging category](../06-Logging-and-Monitoring/var-log.md), [`/var`](var-directory.md), [Files](files.md)

