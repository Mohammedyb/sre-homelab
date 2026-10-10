# `dpkg`

## Overview
`dpkg` is the low-level Debian tool for managing local `.deb` packages; unlike APT, it does not resolve repository dependencies.

## Common Usage
Query package state and use APT to repair missing dependencies when appropriate.
```bash
dpkg -l 'nginx*'
sudo apt -f install
```
Prefer APT for repository installs; reserve direct `dpkg -i` for a vetted local package.

## SRE Relevance
Manual package operations can leave dependencies incomplete or bypass repository policy.
Capture package state during incident diagnosis and reconcile changes through configuration management.

## Quick Examples
`dpkg -L PACKAGE` lists package files; `dpkg -s PACKAGE` reports installed package status.

## Common Flags
| Flag | Description |
| --- | --- |
| `-i FILE.deb` | Install a local Debian package without dependency resolution |
| `-l` | List packages matching a query |

## Related Topics
- [dpkg `-L`](dpkg-l.md)
- [dpkg `-s`](dpkg-s.md)
- [APT](apt.md)
