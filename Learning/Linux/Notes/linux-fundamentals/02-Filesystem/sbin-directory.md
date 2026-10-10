# `/sbin`
## Overview
`/sbin` traditionally contains system-administration executables; modern systems may merge it into `/usr/sbin`.

## Common Usage
Administrative commands may require elevated privileges for system changes. Use least privilege and understand the effect first.

## Bash Example
```bash
ls -ld /sbin; command -v fsck || true
```

Inspects the path and checks whether `fsck` is available; availability depends on the distribution.

## SRE Relevance
Site reliability engineering (SRE) teams should note: System utilities matter in recovery and host maintenance; minimal containers may intentionally omit them.

## Quick Examples
- Check utility: `command -v ip`
- Read its manual: `man fsck`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `|| true` | Keeps an optional availability probe from failing if `fsck` is absent; it does not make `fsck` succeed. |

## Related Topics
[`/bin`](bin-directory.md), [`/usr`](usr-directory.md), [Absolute path](absolute-path.md)

