# `+%F`

## Overview
The `+%F` format passed to `date` prints a date as `YYYY-MM-DD`. It is a convenient ISO-style calendar date.

## Common Usage
```bash
date -u '+%F'
```
This prints the current UTC date, such as `2026-10-09`.

## SRE Relevance
Consistent date formatting helps name backups and filter daily reports. Include time and timezone when a date alone is not precise enough for incident timelines.

## Quick Examples
- `date '+%F %T'` includes local time.
- `date -u '+%FT%TZ'` produces a UTC timestamp with a literal `Z`.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `%F` | Date in `YYYY-MM-DD` format. |
| `+FORMAT` | Ask `date` to format output using conversion directives. |

## Related Topics
- [Date](date.md)
- [Command Substitution](command-substitution.md)
- [Bash Script](../09-Scripting-and-Automation/bash-script.md)
