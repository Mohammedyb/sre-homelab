# `ln -s`
## Overview
`ln -s TARGET LINK_NAME` creates a symbolic link containing a path to another file or directory. The target may be missing and can cross filesystems.

## Common Usage
Choose relative or absolute targets intentionally. Relative targets resolve from the link's containing directory; verify with `readlink`.

## Bash Example
```bash
ln -s ../shared/config.yaml ./config.yaml; readlink ./config.yaml
```

Creates a relative link and prints the stored target path.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Symlink targets can change during deployments or point outside expected roots. Validate links in release layouts and cleanup scripts.

## Quick Examples
- Resolve existing target: `readlink -f ./config.yaml`
- Inspect link: `ls -l ./config.yaml`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-s` | Selects symbolic-link behavior; `-f` on `ln` has separate behavior. |

## Related Topics
[Symbolic link](symbolic-link.md), [Soft link](soft-link.md), [Hard link](hard-link.md)

