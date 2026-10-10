# Pipe Character `|`

## Overview
The pipe character `|` connects one command's standard output to the next command's standard input. It passes data, not command arguments.

## Common Usage
```bash
grep -i error /var/log/app.log | tail -n 20
```
The matching lines flow into `tail`, which limits the displayed results.

## SRE Relevance
Pipelines enable fast diagnosis, but the default pipeline status is often only the last command's status. In Bash automation, use `set -o pipefail` when upstream failures matter.

## Quick Examples
- `ps aux | grep nginx` filters process output (may also match `grep`).
- `sort names.txt | uniq -c` sorts before counting repeated adjacent lines.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `|` is shell syntax, not a command with flags. |

## Related Topics
- [Standard Input](standard-input-stdin.md)
- [Standard Output](standard-output-stdout.md)
- [Grep](grep.md)
