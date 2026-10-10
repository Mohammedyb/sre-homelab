# Debian APT

## Overview
APT (Advanced Package Tool) manages software from Debian-family repositories, resolving package dependencies.
It is commonly used on Debian and Ubuntu systems.

## Common Usage
Refresh repository metadata, then inspect a package candidate before installing.
```bash
sudo apt update
apt policy nginx
```
Metadata refresh does not itself upgrade installed packages; review upgrades separately.

## SRE Relevance
Repository configuration controls package provenance and update cadence.
Use approved mirrors and test upgrades before rolling changes across production.

## Quick Examples
`apt install PACKAGE` installs software; `apt list --upgradable` previews available updates.

## Common Flags
Not applicable; see individual APT command notes for command-specific options.

## Related Topics
- [APT](apt.md)
- [`apt update`](apt-update.md)
- [`apt install`](apt-install.md)
- [PPA](ppa.md)
