# APT

## Overview
APT (Advanced Package Tool) manages packages on Debian-derived Linux distributions; `apt` supports interactive administration, while scripts should use deliberate noninteractive settings.

## Common Usage
Search, inspect, and install packages using configured repositories, as shown here.
```bash
apt search nginx
apt show nginx
sudo apt install nginx
```
Review proposed actions and package source before confirming a production change.

## SRE Relevance
APT operations alter host state and may restart services through package hooks; record versions, use a maintenance plan, and verify health afterward.

## Quick Examples
`apt update` refreshes package indexes; it does not upgrade installed packages.

## Common Flags
| Flag | Description |
| --- | --- |
| `-y` | Automatically answer yes to prompts; use only in reviewed automation |
| `--no-install-recommends` | Avoid installing recommended, non-required packages |

## Related Topics
- [`apt update`](apt-update.md)
- [`apt install`](apt-install.md)
- [`apt search`](apt-search.md) and [`apt show`](apt-show.md)
