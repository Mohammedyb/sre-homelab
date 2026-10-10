# Hard Link

## Overview
A hard link is another directory entry referring to the same index node (inode) and data. It normally must be on the same filesystem and cannot link directories.

## Common Usage
Removing one name does not remove content while another hard link remains. A hard link is not a separate backup copy.

## Bash Example
```bash
ln -- ./data.bin ./data-alias.bin; stat -c 'inode=%i links=%h %n' ./data.bin ./data-alias.bin
```
Matching inode numbers indicate both names reference the same file object.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Hard links can make data appear in multiple places and complicate deduplication and cleanup. Check link counts during disk investigations.

## Quick Examples
- Compare inode numbers: `ls -i ./data.bin ./data-alias.bin`
- Use symlinks for directories or cross-filesystem targets.

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| Plain `ln` | Creates a hard link; add `-s` to create a symbolic link instead. |

## Related Topics
[`ln`](ln.md), [Symbolic link](symbolic-link.md), [Soft link](soft-link.md)
