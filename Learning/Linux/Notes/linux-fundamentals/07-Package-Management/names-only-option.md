# `--names-only`

## Overview
`--names-only` is an option of `apt search` that limits matching to package names rather than descriptions.
It narrows discovery output but does not install or validate a package.

## Common Usage
Search for packages whose names contain a known component.
```bash
apt search --names-only nginx
```
If the desired result is missing, check spelling and refresh indexes with `sudo apt update`.

## SRE Relevance
Focused search reduces noise during incident response, but package provenance still requires review.
Inspect a likely match with `apt show PACKAGE` and `apt policy PACKAGE`.

## Quick Examples
Use `apt search --names-only '^php'` to find package names beginning with `php`.

## Common Flags
| Flag | Description |
| --- | --- |
| `--names-only` | `apt search` option that searches names only |

## Related Topics
- [APT search](apt-search.md)
- [PHP search pattern](php-search-pattern.md)
- [APT show](apt-show.md)
