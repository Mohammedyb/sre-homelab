# Which Command

## Overview
`which` is a utility commonly used to locate an executable found through the shell's `PATH`. Its behavior can vary by platform and shell.

## Common Usage
```bash
which bash
```
The output is typically the path to the selected `bash` executable.

## SRE Relevance
Multiple installed versions of a tool can cause inconsistent automation. Verify the resolved executable and version when debugging hosts or CI runners.

## Quick Examples
- `which python3` finds a likely Python executable.
- In Bash, `type -a command` also reveals aliases, functions, and all matching paths.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | Options vary between `which` implementations; consult local help. |

## Related Topics
- [`which`](which.md)
- [`PATH`](path.md)
- [Binary](binary.md)
