# Less

## Overview
`less` is an interactive pager for reading text without loading it all into a terminal at once. It supports searching and navigation.

## Common Usage
```bash
less /var/log/syslog
```
Use `/pattern` to search forward, `n` to repeat, and `q` to quit.

## SRE Relevance
Use a pager for large logs to avoid overwhelming terminal output. `less` is read-only by default; still avoid exposing secrets in shared sessions.

## Quick Examples
- `less +F app.log` follows appended lines; press `Ctrl+C` to stop following.
- `journalctl -u nginx | less` pages service logs.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-N` | Show line numbers. |
| `-S` | Do not wrap long lines. |

## Related Topics
- [`cat`](cat.md)
- [Head](head.md)
- [Tail](tail.md)
