# Root Directory
## Overview
`/` is the top of the Linux filesystem hierarchy; mounted filesystems are attached beneath it.

## Common Usage
Start at `/` for unambiguous system paths; do not confuse it with `/root`, the root user's home directory.

## Bash Example
```bash
printf 'Root entries: '; printf '%s ' /*; printf '\n'
```

Bash expands `/*` to top-level entries without changing anything.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Understanding the hierarchy helps locate configuration, binaries, logs, and mounted data. Verify mount points before assuming data is on the root disk.

## Quick Examples
- Inspect mounts: `findmnt`
- Check root capacity: `df -h /`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `/` | An absolute path begins at filesystem root; it is not a command flag. |

## Related Topics
[Absolute path](absolute-path.md), [`/etc`](etc-directory.md), [`/var`](var-directory.md)

