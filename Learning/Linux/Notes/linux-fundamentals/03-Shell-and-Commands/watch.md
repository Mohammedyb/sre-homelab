# Watch

## Overview
`watch` repeatedly runs a command and displays refreshed output in a terminal. Its default interval is commonly two seconds.

## Common Usage
```bash
watch -n 5 'df -h /'
```
This refreshes filesystem usage every five seconds; press `Ctrl+C` to stop.

## SRE Relevance
Useful for observing short-lived changes during troubleshooting, but repeated polling can add load. Prefer metrics dashboards or purpose-built monitoring for ongoing production observation.

## Quick Examples
- `watch -n 2 'free -h'` refreshes memory statistics.
- `watch -d 'ss -s'` highlights changes in socket summary output.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-n SECONDS` | Set the refresh interval. |
| `-d` | Highlight differences between updates. |
| `-t` | Hide the header line. |

## Related Topics
- [Date](date.md)
- [Bash](bash.md)
- [Syslog](../06-Logging-and-Monitoring/syslog.md)
