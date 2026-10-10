# Binary

## Overview
A binary is an executable file containing machine-readable instructions. Linux commands may be compiled binaries, scripts, or shell built-ins.

## Common Usage
```bash
file "$(command -v bash)"
```
`file` identifies the resolved Bash file format; command substitution passes its path as one argument.

## SRE Relevance
Verify executable paths, architecture, ownership, and provenance when a tool behaves unexpectedly. Install or replace binaries through trusted package sources.

## Quick Examples
- `command -v tool` reports how the shell resolves `tool`.
- `file /usr/bin/ssh` identifies a known executable without running it.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | Binary is a file type; options belong to inspection commands such as `file`. |

## Related Topics
- [Which Command](which-command.md)
- [`PATH`](path.md)
- [Permissions](../04-Users-and-Permissions/permissions.md)
