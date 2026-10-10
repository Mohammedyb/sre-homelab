# `-r` (Recursive Option)
## Overview
`-r` meaning depends on command: `rm` descends into directories; `cp` copies a directory tree. Recursion may affect many files.

## Common Usage
Before recursion, list the target tree, confirm its root, and avoid elevated privileges unless required.

## Bash Example
```bash
find ./build-output -maxdepth 2 -print
```

This non-destructive preview shows a limited portion of a tree before recursive cleanup.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Recursive commands can cause broad outages. Add path validation, mount boundaries, and dry-run or confirmation steps to automation.

## Quick Examples
- Copy directory: `cp -r ./config ./config.copy`
- Remove after review: `rm -r -- ./obsolete-tree`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-r` | Command-specific; with `rm`, deletes descendants. Prefer `rmdir` when only empty directories should be removed. |

## Related Topics
[`rm`](rm.md), [`cp`](cp.md), [`rmdir`](rmdir.md)

