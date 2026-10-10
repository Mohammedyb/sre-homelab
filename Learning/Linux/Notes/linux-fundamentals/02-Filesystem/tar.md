# `tar`
## Overview
`tar` creates and reads archives bundling paths and metadata. Compression is optional; a tar archive is not inherently compressed.

## Common Usage
List contents before extraction, choose a safe destination, and treat untrusted archives cautiously because of unexpected paths or links.

## Bash Example
```bash
tar -tf backup.tar
```

Lists archive members without extracting them.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Archives support backups and artifact transfer. Validate contents, permissions, ownership, free space, and restore procedures.

## Quick Examples
- Create archive: `tar -cf backup.tar ./config`
- Extract to destination: `tar -xf backup.tar -C ./restore`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-c`, `-t`, `-x`, `-f` | Create, list, extract, and specify archive filename respectively. See [`-czf`](tar-czf.md). |

## Related Topics
[`-czf`](tar-czf.md), [`gzip`](gzip.md), [Files](files.md)

