# `-p` (`mkdir` Parents Option)
## Overview
`mkdir -p` creates missing parent directories and succeeds if the requested directory already exists. It does not validate existing ownership or modes.

## Common Usage
Use for repeatable setup, then verify ownership and permissions where security matters.

## Bash Example
```bash
mkdir -p -m 0750 ./state/cache
```

Creates the path as needed and requests mode for directories created; existing parent modes are not rewritten.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Idempotent setup aids deployments, but check pre-existing paths and symlinks in untrusted locations.

## Quick Examples
- Create paths: `mkdir -p ./logs ./data/archive`
- Verify: `stat -c '%A %U:%G %n' ./state/cache`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-p` | Creates parent directories; it does not mean recursive deletion. |

## Related Topics
[`mkdir`](mkdir.md), [`-r` recursive option](recursive-option.md), [Directories](directories.md)

