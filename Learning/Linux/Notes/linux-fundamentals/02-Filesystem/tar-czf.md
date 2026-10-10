# `-czf`
## Overview
In `tar -czf ARCHIVE.tar.gz PATH`, `-c` creates, `-z` compresses with gzip, and `-f` supplies the archive filename immediately after it.

## Common Usage
Use an explicit archive path and inspect members before relying on a backup. Creating the archive does not remove source files.

## Bash Example
```bash
tar -czf config-backup.tar.gz ./config; tar -tzf config-backup.tar.gz
```

Creates a gzip-compressed archive, then lists its contents for verification.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Compressed archives support snapshots and transfers. Monitor integrity, retention, access control, and restore testing.

## Quick Examples
- Extract: `tar -xzf config-backup.tar.gz -C ./restore`
- Uncompressed archive: `tar -cf config-backup.tar ./config`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-c`, `-z`, `-f` | Create, gzip-compress, and name the archive. `-t` lists; `-x` extracts. Never extract untrusted archives into privileged paths. |

## Related Topics
[`tar`](tar.md), [`gzip`](gzip.md), [Files](files.md)

