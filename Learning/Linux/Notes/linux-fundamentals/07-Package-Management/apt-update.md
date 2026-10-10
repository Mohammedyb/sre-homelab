# `apt update`

## Overview
`apt update` is an APT (Advanced Package Tool) subcommand that refreshes local repository indexes without upgrading installed package versions.

## Common Usage
Refresh indexes before checking candidates or installing a package.
```bash
sudo apt update
apt list --upgradable
```
In a deployment, check output for failed or unsigned repositories before relying on package results.

## SRE Relevance
Stale indexes can hide security fixes or produce confusing package-resolution errors.
Alert on repository failures and use trusted mirrors.

## Quick Examples
After a successful update, inspect a candidate with `apt policy PACKAGE`.

## Common Flags
| Flag | Description |
| --- | --- |
| `-o` | Override an APT configuration value for this invocation |
| `--error-on=any` | Return an error if any repository update fails, where supported |

## Related Topics
- [APT](apt.md)
- [`apt install`](apt-install.md)
- [APT help](apt-help.md)
