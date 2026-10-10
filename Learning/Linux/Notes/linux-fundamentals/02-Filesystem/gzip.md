# `gzip`
## Overview
`gzip` compresses files, usually replacing the input with `.gz` unless configured to keep it. It is commonly combined with `tar` for directory archives.

## Common Usage
Use `-k` when the original must remain and verify compressed data before removing or rotating source data.

## Bash Example
```bash
gzip -k ./access.log; gzip -t ./access.log.gz
```

Compresses while keeping the source, then tests compressed-file integrity.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Compression reduces log and artifact storage but costs central processing unit (CPU). Apply established rotation and retention policies to active logs.

## Quick Examples
- Decompress: `gzip -d ./access.log.gz`
- View text: `zcat ./access.log.gz | head`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-k`, `-t`, `-d` | Keep input, test integrity, and decompress respectively. |

## Related Topics
[`tar`](tar.md), [`-czf`](tar-czf.md), [`/var/log`](var-log.md)

