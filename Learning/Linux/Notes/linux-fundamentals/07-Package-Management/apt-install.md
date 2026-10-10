# `apt install`

## Overview
`apt install` is an APT (Advanced Package Tool) subcommand that installs or updates named packages and dependencies, including a requested available version.

## Common Usage
Install a production utility after refreshing indexes and checking the candidate.
```bash
sudo apt update
apt policy curl
sudo apt install curl
```
Review the package plan because dependencies and package scripts can change host behavior.

## SRE Relevance
An install can modify files, trigger service actions, or pull transitive dependencies; use tested images or staged rollouts across a fleet.

## Quick Examples
`sudo apt install PACKAGE=VERSION` requests a specific available version; confirm the repository provides it first.

## Common Flags
| Flag | Description |
| --- | --- |
| `-y` | Automatically answer yes to prompts; use only in controlled automation |
| `--no-install-recommends` | Skip recommended packages that are not required dependencies |

## Related Topics
- [APT](apt.md)
- [`apt update`](apt-update.md)
- [APT show](apt-show.md)
