# `apt search`

## Overview
`apt search` searches package names and descriptions in the local APT (Advanced Package Tool) indexes.
Run `apt update` first when search results may be stale.

## Common Usage
Find packages related to a service and inspect candidates before installation.
```bash
sudo apt update
apt search nginx
```
Use the focused name-only option when a broad description search produces too much output.

## SRE Relevance
Package search is useful for discovery but does not verify package trust, compatibility, or installed state.
Confirm source and version with `apt show` or `apt policy`.

## Quick Examples
`apt search 'php.*fpm'` searches matching indexed package text; use quoted expressions to avoid shell expansion.

## Common Flags
| Flag | Description |
| --- | --- |
| `--names-only` | `apt search` option that matches package names only |

## Related Topics
- [Names-only option](names-only-option.md)
- [PHP search pattern](php-search-pattern.md)
- [APT show](apt-show.md)
