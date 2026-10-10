# `^php`

## Overview
`^php` is a regular-expression search pattern that matches text beginning with `php`.
With `apt search --names-only`, it targets package names whose first characters are `php`.

## Common Usage
Quote the pattern so the shell passes it intact to APT.
```bash
apt search --names-only '^php'
```
This can discover PHP (PHP: Hypertext Preprocessor) runtime packages and extensions; verify package details before selecting one.

## SRE Relevance
Pattern-based discovery helps find versioned runtimes and extensions without broad description matches.
Confirm the selected version matches application and repository support requirements.

## Quick Examples
Use `apt show php-fpm` to inspect a candidate and `apt policy php-fpm` to review its source.

## Common Flags
| Flag | Description |
| --- | --- |
| `--names-only` | `apt search` option needed to limit this pattern to package names |

## Related Topics
- [APT search](apt-search.md)
- [Names-only option](names-only-option.md)
- [APT show](apt-show.md)
