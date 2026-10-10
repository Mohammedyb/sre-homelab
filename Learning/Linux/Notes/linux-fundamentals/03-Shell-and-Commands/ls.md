# `ls`
## Overview
- `ls` lists files and directories in the current or specified location.
- It helps verify deployment artifacts, configuration files, and directory contents.
- Output is a human-readable view; scripts should use safer file tests than parsing it.
## Common Usage
```bash
ls -la /etc
```
Lists all entries, including hidden ones, in long format.
## SRE Relevance
- Check whether expected files or mount points are present during triage.
- Compare directory contents before and after a deployment.
- Use `stat` or shell file tests for precise automation checks.
## Quick Examples
- `ls /var/log` - inspect available log files.
- `ls -lh /var/log` - show sizes in a readable format.
## Common Flags
| Flag | Description |
| --- | --- |
| `-l` | Long format with permissions, owner, size, and time |
| `-a` | Include hidden entries |
| `-h` | Show sizes in human-readable units; commonly combined with `-l` |
| `-t` | Sort by modification time |
## Related Topics
- [`pwd`](pwd.md)
- [`cd`](cd.md)
- [`ls -l`](ls-l.md)
- [CSV filename glob](../02-Filesystem/ls-csv-glob.md)

