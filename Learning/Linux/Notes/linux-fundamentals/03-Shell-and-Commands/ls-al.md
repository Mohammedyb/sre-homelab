# `ls -al`

## Overview
- `ls -al` combines `-a` (include hidden entries) and `-l` (long format).
- It reveals dotfiles such as shell configuration and displays their metadata.
- Hidden files are not inherently private; permissions still control access.
## Common Usage
```bash
ls -al /home/service
```
Shows all entries, including dotfiles, with ownership and permission details.
## SRE Relevance
- Find hidden application configuration, caches, and deployment files.
- Diagnose unexpected permissions on a service account's dotfiles.
- Avoid exposing sensitive output in shared logs or support tickets.
## Quick Examples
- `ls -al ~` - inspect files in the current user's home directory.
- `ls -al /etc` - include hidden entries in a system configuration directory.
- `ls -alh /var/log` - show all entries and readable sizes.
## Common Flags
| Flag | Description |
| --- | --- |
| `-a` | Include hidden entries whose names start with `.` |
| `-l` | Show long-format metadata |
| `-h` | Human-readable sizes, typically combined with `-l` |
## Related Topics
- [`ls`](ls.md)
- [`ls -l`](ls-l.md)
- [Dotfiles and `.bashrc`](../04-Users-and-Permissions/bashrc.md)

