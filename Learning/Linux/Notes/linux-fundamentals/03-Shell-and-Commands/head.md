# Head

## Overview
`head` prints the beginning of one or more files, ten lines by default. It is useful for quickly checking file structure or recent output.

## Common Usage
```bash
head -n 20 /var/log/app.log
```
This prints the first 20 lines, limiting output during initial inspection.

## SRE Relevance
Use bounded output to inspect large files safely. For timestamped logs, remember that the start of a file may not contain the latest incident data.

## Quick Examples
- `head -n 1 config.csv` checks a header.
- `head -c 128 file.bin` inspects a small byte prefix; binary output may be unreadable.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-n N` | Print the first N lines. |
| `-c N` | Print the first N bytes. |

## Related Topics
- [Tail](tail.md)
- [Less](less.md)
- [CSV](../02-Filesystem/csv.md)
