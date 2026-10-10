# `-L` (tree Depth Option)
## Overview
For `tree`, `-L N` limits output to at most `N` directory levels below the starting point. It limits traversal display, not filesystem size or permissions.

## Common Usage
Start shallow for quick inventory and increase depth only when needed.

## Bash Example
```bash
tree -L 1 /var
```

Displays `/var` and one level of entries beneath it.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Depth limits make incident-time inspection readable and reduce needless output from broad trees.

## Quick Examples
- Two levels: `tree -L 2 /etc`
- Shallow directories: `tree -d -L 1 /srv`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-L 1` | An argument to `tree` that limits depth; it is not a universal shell option. |

## Related Topics
[`tree`](tree.md), [Directories](directories.md), [`/var`](var-directory.md)

