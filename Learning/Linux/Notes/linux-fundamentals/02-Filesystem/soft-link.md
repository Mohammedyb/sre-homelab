# Soft Link
## Overview
A soft link is another name for a symbolic link: a filesystem object storing a path to a file or directory. It can dangle if the target disappears.

## Common Usage
Create with `ln -s`; inspect the link without following it using `ls -l` or `readlink`.

## Bash Example
```bash
ln -s /etc/hosts ./hosts-link; ls -l ./hosts-link
```

Creates a soft link to `/etc/hosts` and displays the link and its target.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Links often support release switching and shared configuration. Check for dangling targets and ensure destinations meet access-control expectations.

## Quick Examples
- Read stored target: `readlink ./hosts-link`
- Check target: `test -e ./hosts-link && echo target-present`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `ln -s` | Creates a symbolic (soft) link; `-L` in other commands is command-specific and may mean follow links. |

## Related Topics
[Symbolic link](symbolic-link.md), [`ln -s`](ln-s.md), [Hard link](hard-link.md)

