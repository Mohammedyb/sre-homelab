# `mv` Command
## Overview
`mv` moves or renames files and directories. Across filesystems it may copy and then remove data rather than changing one directory entry.

## Common Usage
Confirm source and destination, especially if a destination directory exists. Use interactive protection when overwrite is unintended.

## Bash Example
```bash
mv -i -- ./app.conf ./app.conf.disabled
```

Renames the file and prompts if the destination would be overwritten.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Renaming active configuration may affect services immediately. Use controlled rollout, rollback copies, and validate resulting paths and permissions.

## Quick Examples
- Move into directory: `mv -- report.csv ./archive/`
- Inspect result: `ls -l -- ./app.conf.disabled`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-i`, `--` | `-i` prompts before overwriting; `--` ends option parsing for dash-leading paths. |

## Related Topics
[`cp`](cp.md), [`rm`](rm.md), [Absolute path](absolute-path.md)

