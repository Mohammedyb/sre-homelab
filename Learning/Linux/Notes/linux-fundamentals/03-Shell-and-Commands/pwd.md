# `pwd`

## Overview
`pwd` means **print working directory**. It displays the absolute path of the shell's current directory.

## Common Usage
```bash
pwd
```
Run it before relative-path commands to verify the target location.

## SRE Relevance
Wrong working directories can cause scripts or cleanup commands to affect unintended files. Use `pwd` in troubleshooting and deployment checks.

## Quick Examples
- `pwd -P` prints the physical path without resolving symbolic links.
- `printf 'Working in: %s\n' "$PWD"` prints the shell's path variable.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-L` | Show the logical path, including symbolic links (commonly the default). |
| `-P` | Resolve symbolic links and show the physical path. |

## Related Topics
- [`cd`](cd.md)
- [Command Line](command-line.md)
- [Absolute paths](../02-Filesystem/absolute-path.md)
