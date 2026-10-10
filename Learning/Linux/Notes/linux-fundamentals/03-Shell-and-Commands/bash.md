# Bash

## Overview
Bash (Bourne Again SHell) is a widely used command interpreter and scripting language on Linux systems.

## Common Usage
```bash
bash --version
```
This checks the installed Bash version; interactive commands and scripts run by Bash may use different startup configuration.

## SRE Relevance
Bash is common in operations automation, but scripts should use explicit error handling and predictable environments. Prefer POSIX shell when Bash-specific features are unnecessary.

## Quick Examples
- `bash script.sh` runs a script with Bash.
- `set -o pipefail` makes a pipeline report failure from any command in it.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-n` | Parse a script without executing it (syntax check). |
| `-x` | Trace expanded commands; avoid with secrets. |

## Related Topics
- [Shells](shells.md)
- [Bash Script](../09-Scripting-and-Automation/bash-script.md)
- [Exit Codes](../09-Scripting-and-Automation/exit-codes.md)
