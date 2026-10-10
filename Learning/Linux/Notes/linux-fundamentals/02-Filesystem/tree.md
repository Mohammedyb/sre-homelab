# `tree`
## Overview
`tree` displays directory contents as an indented hierarchy. It may need separate installation and can produce huge output from broad roots.

## Common Usage
Choose a narrow starting path and depth, especially on production hosts and large repositories.

## Bash Example
```bash
tree -L 2 /etc
```

Displays `/etc` and descendants through two directory levels.

## SRE Relevance
Site reliability engineering (SRE) teams should note: A bounded tree view quickly explains configuration or deployment layouts. Avoid sharing sensitive path names publicly.

## Quick Examples
- Directories only: `tree -d -L 2 .`
- Check availability: `command -v tree`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-L N`, `-d` | `-L` limits displayed depth; `-d` shows directories only. See [`-L`](tree-depth-option.md). |

## Related Topics
[`-L`](tree-depth-option.md), [Directories](directories.md), [`ls`](../03-Shell-and-Commands/ls.md)

