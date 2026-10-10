# Tail

## Overview
`tail` prints the end of a file, ten lines by default. It can follow a file as new lines are appended.

## Common Usage
```bash
tail -n 50 /var/log/app.log
```
This shows the last 50 lines, a bounded starting point for log inspection.

## SRE Relevance
Following logs helps diagnose active incidents, but log rotation can replace or rename files. For managed services, prefer `journalctl` or the platform's log collector.

## Quick Examples
- `tail -f app.log` follows appended data; stop with `Ctrl+C`.
- `tail -n 100 app.log | grep -i error` filters a recent slice.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-n N` | Print the last N lines. |
| `-f` | Follow appended output. |
| `-F` | Follow by name and retry across rotation (implementation-dependent). |

## Related Topics
- [Head](head.md)
- [Less](less.md)
- [Syslog](../06-Logging-and-Monitoring/syslog.md)
