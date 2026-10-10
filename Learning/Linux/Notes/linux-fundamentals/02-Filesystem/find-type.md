# `-type` (`find`)
## Overview
The `find` predicate `-type` filters filesystem objects. Common values: `f` regular files, `d` directories, and `l` symbolic links.

## Common Usage
Combine it with a narrow starting path and other predicates to make searches relevant and safe.

## Bash Example
```bash
find /etc -maxdepth 2 -type f -name '*.conf' -print
```

Lists regular `.conf` files within two levels of `/etc`.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Type filters distinguish files, directories, and links during configuration audits and path troubleshooting.

## Quick Examples
- Directories: `find . -type d -print`
- Symlinks: `find . -type l -print`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-type f`, `-type d`, `-type l` | Selects regular files, directories, and symbolic links respectively. |

## Related Topics
[`find`](find.md), [Directories](directories.md), [Symbolic link](symbolic-link.md)

