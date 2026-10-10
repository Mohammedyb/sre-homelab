# Symbolic Link
## Overview
A symbolic link (symlink) is a filesystem object storing a path. It can reference files or directories on another filesystem, using relative or absolute paths.

## Common Usage
Use `readlink` for the stored path and `readlink -f` to resolve an existing target. Do not assume the target exists.

## Bash Example
```bash
ln -s /var/log ./logs-link; readlink -f ./logs-link
```

Creates a symlink and resolves its destination for inspection.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Symlinked release paths support version switching, but test atomicity, ownership, and rollback with the deployment system.

## Quick Examples
- Identify link: `test -L ./logs-link && echo symlink`
- List without following: `ls -ld ./logs-link`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `ln -s` | Creates a symbolic link; `-L` options on other commands may mean follow links. |

## Related Topics
[Soft link](soft-link.md), [`ln -s`](ln-s.md), [Hard link](hard-link.md)

