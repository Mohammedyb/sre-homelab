# `--remove`

## Overview
`--remove` is an option of `add-apt-repository` that removes a configured repository or PPA.
It is not a general APT option for uninstalling packages.

## Common Usage
Remove a repository by specifying the same identifier that was used to add it.
```bash
sudo add-apt-repository --remove ppa:OWNER/ARCHIVE
sudo apt update
```
Confirm the repository entry is gone and check whether installed packages still depend on it.

## SRE Relevance
Removing a source prevents future package retrieval from that archive but does not automatically downgrade packages already installed.
Plan package version and dependency cleanup separately.

## Quick Examples
Use `grep -R` under `/etc/apt/sources.list.d/` to inspect remaining source entries.

## Common Flags
| Flag | Description |
| --- | --- |
| `--remove REPOSITORY` | `add-apt-repository` option that removes the named source |

## Related Topics
- [Add APT repository](add-apt-repository.md)
- [PPA](ppa.md)
- [APT](apt.md)
