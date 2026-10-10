# `cp`
## Overview
`cp` copies files and, with suitable options, directories. A destination can be overwritten; inspect both paths first.

## Common Usage
Quote paths and consider metadata and symlink behavior. For directory copies specify recursion; avoid copying a path onto itself.

## Bash Example
```bash
cp -i -- ./app.conf ./app.conf.backup
```

Copies a configuration file and prompts before overwriting the backup destination.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Create verified backups before risky changes and check free space. Preserve needed ownership and metadata through deployment tooling.

## Quick Examples
- Copy a directory: `cp -a ./config ./config.backup`
- Compare copies: `diff -u ./app.conf ./app.conf.backup`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-i`, `-a` | `-i` prompts before overwrite; `-a` copies recursively and preserves common metadata and symlinks. |

## Related Topics
[Files](files.md), [`mv`](mv-command.md), [`rm`](rm.md)

