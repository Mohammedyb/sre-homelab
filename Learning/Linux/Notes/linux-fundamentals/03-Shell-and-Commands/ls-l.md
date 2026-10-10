# `ls -l`

## Overview
- `ls -l` lists directory entries in long format.
- It shows permissions, link count, owner, group, size, modification time, and name.
- Use it for a quick operational check; `stat` provides more detailed metadata.
## Common Usage
```bash
ls -l /etc/ssh/sshd_config
```
Shows ownership and permissions for the SSH server configuration file.
## SRE Relevance
- Investigate access failures by checking file owners and mode bits.
- Confirm that deployed configuration has the expected ownership.
- Pair with `stat` when timestamps or inode details matter.
## Quick Examples
- `ls -l /var/log` - inspect log ownership and sizes.
- `ls -lh` - show long output with readable sizes.
## Common Flags
| Flag | Description |
| --- | --- |
| `-l` | Display long-format metadata |
| `-h` | Display sizes in human-readable units with `-l` |
| `-a` | Include hidden entries |
## Related Topics
- [`ls`](ls.md)
- [`ls -al`](ls-al.md)
- [Permissions](../04-Users-and-Permissions/permissions.md)
- [`chmod`](../04-Users-and-Permissions/chmod.md)
