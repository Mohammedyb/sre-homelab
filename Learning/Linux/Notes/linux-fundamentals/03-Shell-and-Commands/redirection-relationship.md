# `>` and `>>` Relationship

## Overview
Both `>` and `>>` redirect standard output to a file. The key difference is that `>` truncates an existing file, while `>>` appends.

## Common Usage
```bash
printf '%s\n' 'latest status' >> status.log
```
Use `>>` when preserving earlier output is intentional; use `>` only when replacing the destination is safe.

## SRE Relevance
Confusing these operators can erase diagnostic evidence or create unbounded logs. Review redirection targets during change review and apply log rotation.

## Quick Examples
- `command > result.txt` replaces the file contents.
- `command >> result.txt` adds output after existing contents.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | These operators are shell syntax; neither has flags. |

## Related Topics
- [`>` (redirection)](redirection.md)
- [`>>` (append redirection)](append-redirection.md)
- [Standard Output](standard-output-stdout.md)
