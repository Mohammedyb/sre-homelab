# `./`

## Overview
The prefix `./` refers to the current directory. It is commonly used to run a local executable or identify a local file explicitly.

## Common Usage
```bash
./health-check.sh
```
This runs the script from the current directory when it is executable and its interpreter is available.

## SRE Relevance
Explicit `./` prevents confusion with a different executable found earlier in `PATH`. Inspect local scripts before executing them, especially on production hosts.

## Quick Examples
- `cat ./config.yaml` reads a file in the current directory.
- `bash ./script.sh` runs a local script using Bash without requiring executable permission.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `./` is a relative path prefix, not a command option. |

## Related Topics
- [`cd`](cd.md)
- [`PATH`](path.md)
- [Bash Script](../09-Scripting-and-Automation/bash-script.md)
