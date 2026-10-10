# `apt --help`

## Overview
`--help` is an option of the `apt` command that prints a concise usage summary and available subcommands.
It is useful for a quick reminder; detailed behavior is documented in manual pages.

## Common Usage
Display help on the target host before using unfamiliar APT syntax.
```bash
apt --help
man apt
```
Check local help because supported options can vary between APT versions.

## SRE Relevance
Using version-matched local documentation reduces mistakes during maintenance and incident response.
For scripted behavior, consult the subcommand's manual and test on the same distribution release.

## Quick Examples
Use `apt --help` for the command summary and `man apt-get` for lower-level command details.

## Common Flags
| Flag | Description |
| --- | --- |
| `--help` | `apt` option that prints command usage and exits |

## Related Topics
- [APT](apt.md)
- [APT search](apt-search.md)
- [`apt install`](apt-install.md)
