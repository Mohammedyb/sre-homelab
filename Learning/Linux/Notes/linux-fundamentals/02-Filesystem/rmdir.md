# `rmdir`
## Overview
`rmdir` removes empty directories only. It is safer than recursive removal when a directory is expected to contain no files.

## Common Usage
If it refuses, inspect contents rather than forcing deletion. Specify the exact directory and avoid uncertain globs.

## Bash Example
```bash
rmdir -- ./empty-staging
```

Removes `empty-staging` only if empty; it fails without deleting non-empty contents.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Empty-only removal reduces accidental loss. Unexpected contents may indicate a failed job or retained evidence and should be investigated.

## Quick Examples
- Inspect contents: `find ./empty-staging -mindepth 1 -maxdepth 1 -print`
- Remove empty parents too: `rmdir -p ./a/b/c`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-p` | Also removes parent directories if empty; it still does not recursively delete contents. |

## Related Topics
[`rm`](rm.md), [`mkdir`](mkdir.md), [Directories](directories.md)

