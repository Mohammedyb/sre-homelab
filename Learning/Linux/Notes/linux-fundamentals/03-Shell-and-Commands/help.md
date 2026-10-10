# `--help`

## Overview
`--help` is a common convention for requesting brief command usage information. Not every program supports it or formats it consistently.

## Common Usage
```bash
grep --help
```
This prints a command summary and common options without performing a search.

## SRE Relevance
Check the installed tool's supported options before using flags in production scripts. Local help reflects the version actually present on the host.

## Quick Examples
- `tar --help` summarizes syntax for the installed `tar`.
- `command --help | less` pages long help output.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `--help` | Request usage information when supported. |

## Related Topics
- [Man](man.md)
- [Command Line](command-line.md)
- [Grep](grep.md)
