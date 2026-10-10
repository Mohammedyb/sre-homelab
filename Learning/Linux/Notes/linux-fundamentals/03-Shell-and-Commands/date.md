# Date

## Overview
`date` displays or formats the system's current date and time. It can also parse and convert dates, with differences between implementations.

## Common Usage
```bash
date '+%F %T %Z'
```
This prints the ISO-style calendar date, time, and timezone abbreviation.

## SRE Relevance
Correct clocks and time zones are essential for correlating distributed logs. Use UTC in shared automation where possible and investigate clock synchronization issues.

## Quick Examples
- `date -u` displays time in UTC.
- `date -Is` emits an ISO 8601 timestamp on common GNU systems.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-u` | Use Coordinated Universal Time (UTC). |
| `-d STRING` | Parse a date string on GNU systems; not portable to all platforms. |

## Related Topics
- [`+%F`](date-format-f.md)
- [Command Substitution](command-substitution.md)
- [Syslog](../06-Logging-and-Monitoring/syslog.md)
