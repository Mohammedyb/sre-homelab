# `cd`

## Overview
`cd` means **change directory**. It changes the current directory of the running shell.

## Common Usage
```bash
cd /var/log
```
This moves the shell to `/var/log`; it does not launch a separate process.

## SRE Relevance
Relative paths depend on the current directory. Check with `pwd` before running maintenance scripts or file operations.

## Quick Examples
- `cd ..` moves to the parent directory.
- `cd -` returns to the previous directory; `cd ~` goes to the home directory.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-L` | Follow symbolic links logically (usual behavior). |
| `-P` | Resolve symbolic links physically. |

## Related Topics
- [`pwd`](pwd.md)
- [Absolute paths](../02-Filesystem/absolute-path.md)
- [Users](../04-Users-and-Permissions/users.md)
