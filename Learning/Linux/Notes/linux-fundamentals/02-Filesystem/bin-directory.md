# `/bin`
## Overview
`/bin` traditionally stores essential user commands. On many modern systems it is a symlink into `/usr/bin` (merged-`/usr` layout).

## Common Usage
Use `command -v` to locate executables; do not assume the same physical layout on every distribution.

## Bash Example
```bash
ls -ld /bin; command -v ls
```

Shows whether `/bin` is a directory or symlink and locates the shell-selected `ls` executable.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Rescue environments and early-boot tools rely on essential commands. Know the merged-/usr layout when troubleshooting boot or containers.

## Quick Examples
- Inspect target: `readlink /bin`
- Locate shell: `command -v sh`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `ls -d` | Shows `/bin` itself, including whether it is a symlink. |

## Related Topics
[`/usr`](usr-directory.md), [`/sbin`](sbin-directory.md), [Symbolic link](symbolic-link.md)

