# `ln`

## Overview
Plain `ln` creates a hard link: another directory entry to the same file data on the same filesystem. Both names refer to the same index node (inode). Ordinary users generally cannot hard-link directories.

## Common Usage
Both names share content and inode; modifying either changes the same file. Removing one name leaves data while another link remains.

## Bash Example
```bash
ln -- ./source.dat ./source-link.dat; ls -li ./source.dat ./source-link.dat
```
Creates another name for the file and displays inode numbers to show their identity.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Hard links complicate backups, cleanup, and storage accounting. Check filesystem boundaries and link counts when diagnosing disk usage.

## Quick Examples
- Show link count: `stat -c '%h %n' ./source.dat`
- Use `ln -s` when a path reference is intended.

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-s` | Changes `ln` from a hard link to a symbolic link; without it the default is a hard link. |

## Related Topics
[`ln -s`](ln-s.md), [Hard link](hard-link.md), [Symbolic link](symbolic-link.md)
