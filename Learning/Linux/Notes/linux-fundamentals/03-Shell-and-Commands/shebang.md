# Shebang `#!`

## Overview
A shebang is the first line of an executable script, beginning with `#!`, that identifies its interpreter.

## Common Usage
```bash
#!/usr/bin/env bash
printf 'health check\n'
```
Save the line as the file's first bytes, then mark the script executable to run it directly.

## SRE Relevance
An explicit interpreter avoids accidental execution under an incompatible shell. `/usr/bin/env` finds Bash through `PATH`; use a trusted, controlled environment.

## Quick Examples
- `#!/bin/sh` requests the system's POSIX shell.
- `bash script.sh` selects Bash directly and does not require an executable shebang.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `#!` is script syntax, not a command with flags. |

## Related Topics
- [Bash Script](../09-Scripting-and-Automation/bash-script.md)
- [Bash](bash.md)
- [`./`](dot-slash.md)
