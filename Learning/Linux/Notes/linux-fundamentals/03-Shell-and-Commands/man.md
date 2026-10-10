# Man

## Overview
`man` displays manual pages documenting commands, system calls, file formats, and administration topics.

## Common Usage
```bash
man grep
```
Navigate with pager controls, search using `/term`, and press `q` to quit.

## SRE Relevance
Manual pages are authoritative for the installed system's command behavior. Check distribution and version differences before copying options between hosts.

## Quick Examples
- `man 5 passwd` opens the section about the passwd file format.
- `man -k network` searches manual page descriptions.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-k` | Search manual page names and descriptions. |
| `-f` | Show a short description for a named page. |

## Related Topics
- [`--help`](help.md)
- [Less](less.md)
- [Command Line](command-line.md)
