# `0` (stdin file descriptor)

## Overview
File descriptor `0` is the conventional descriptor for standard input (stdin). A file descriptor is a small integer a process uses to refer to an open stream or file.

## Common Usage
```bash
wc -l 0< input.txt
```
`0<` explicitly redirects `input.txt` to stdin; the `0` is usually omitted because stdin is the default.

## SRE Relevance
Explicit descriptors clarify complex redirections in scripts. Understand which stream a command consumes before wiring it into automation.

## Quick Examples
- `command < input.txt` is shorthand for descriptor `0`.
- `read -r value < config.txt` reads redirected input in Bash.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `0` is a file descriptor, not a command option. |

## Related Topics
- [Standard Input](standard-input-stdin.md)
- [`1` (stdout file descriptor)](fd-1-stdout.md)
- [Pipe Character `|`](pipe-character.md)
