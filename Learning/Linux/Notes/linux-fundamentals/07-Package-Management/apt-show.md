# `apt show`

## Overview
`apt show` displays metadata for a package in configured APT (Advanced Package Tool) indexes, including version, dependencies, description, and source.

## Common Usage
Inspect a package before installing or updating it.
```bash
apt show nginx
apt policy nginx
```
Refresh indexes first if the displayed candidate may be outdated.

## SRE Relevance
Package metadata helps verify provenance, dependencies, and version before a production change.
Compare the candidate to the approved repository and compatibility requirements.

## Quick Examples
`apt show PACKAGE=VERSION` can inspect a specific indexed version when supported by the local APT version.

## Common Flags
| Flag | Description |
| --- | --- |
| `-a` | Show all available versions of a package |
| `--no-all-versions` | Show only the candidate version |

## Related Topics
- [APT](apt.md)
- [APT search](apt-search.md)
- [`apt install`](apt-install.md)
