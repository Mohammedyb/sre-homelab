# Command Line

## Overview
The command line is a text-based way to give a computer commands. A command commonly has a program, options, and arguments.

## Common Usage
```bash
ls -lah /var/log
```
`ls` is the program, `-lah` are options, and `/var/log` is its argument.

## SRE Relevance
Command-line tools are composable and automatable, but quoting and exact targets matter. Prefer read-only inspection before changing state.

## Quick Examples
- `command --help` often summarizes supported options.
- Quote paths containing spaces: `cat "service logs.txt"`.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | Flags are specific to each command. |

## Related Topics
- [Terminal](terminal.md)
- [Shells](shells.md)
- [Pipe Character `|`](pipe-character.md)
