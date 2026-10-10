# Directories
## Overview
A directory maps names to filesystem objects and organizes paths. `.` and `..` refer to current and parent directories; `/` is the hierarchy root.

## Common Usage
Use `pwd` to confirm context and quote paths with spaces. Relative paths are interpreted from the process working directory.

## Bash Example
```bash
pwd; find . -maxdepth 1 -type d -print
```

Prints the current location and directories immediately beneath it.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Working-directory assumptions often break jobs and service scripts. Use explicit working directories and verify permissions on parent paths.

## Quick Examples
- Show parent: `dirname /var/log/syslog`
- Change location: `cd /var/log`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `find -maxdepth 1 -type d` | Limits traversal to immediate directory entries. |

## Related Topics
[Root directory](root-directory.md), [Absolute path](absolute-path.md), [`mkdir`](mkdir.md)

