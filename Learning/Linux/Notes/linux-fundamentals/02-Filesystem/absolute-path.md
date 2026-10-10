# Full File System Address (Absolute Path)
## Overview
An absolute path names a location from `/` and is independent of the current working directory. Example: `/var/log/syslog`.

## Common Usage
Use absolute paths in service configuration and automation when the target must be explicit; confirm existence and permissions.

## Bash Example
```bash
pwd; ls -ld /var/log
```

`pwd` shows the current directory; `ls` uses an absolute path regardless of that directory.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Absolute paths prevent failures caused by a service's different working directory, especially in scheduled jobs and containers.

## Quick Examples
- Resolve a path: `readlink -f /etc/hosts`
- Check directory: `test -d /var/log && echo exists`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| Leading `/` | Anchors path lookup at the filesystem root; relative paths use the current working directory. |

## Related Topics
[Root directory](root-directory.md), [Directories](directories.md), [`find`](find.md)

