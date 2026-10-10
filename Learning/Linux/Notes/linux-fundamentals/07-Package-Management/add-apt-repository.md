# `add-apt-repository`

## Overview
`add-apt-repository` adds or removes configured APT (Advanced Package Tool) repositories on supported Debian-family systems; it often manages Ubuntu PPAs.

## Common Usage
Add a repository only after validating its publisher, signing key, and release compatibility.
```bash
sudo add-apt-repository ppa:OWNER/ARCHIVE
sudo apt update
```
Review the repository entry and package candidates before installing from it.

## SRE Relevance
Adding a repository changes package provenance and future upgrade behavior for the host.
Document its owner, purpose, key rotation, and removal plan.

## Quick Examples
`sudo add-apt-repository --remove ppa:OWNER/ARCHIVE` removes a configured PPA.

## Common Flags
| Flag | Description |
| --- | --- |
| `--remove` | Option of `add-apt-repository` that removes the specified repository |
| `-y` | Skip confirmation prompts; use only in reviewed automation |

## Related Topics
- [PPA](ppa.md)
- [Remove option](remove-option.md)
- [`apt update`](apt-update.md)
