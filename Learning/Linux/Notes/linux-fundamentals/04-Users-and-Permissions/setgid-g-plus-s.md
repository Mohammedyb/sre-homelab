# `g+s`

## Overview
The set-group-ID bit on a directory makes new entries inherit its group; it does not itself grant group write access.
## Common Usage
```bash
chmod g+s /srv/releases
```
Verify that the intended group owns new files created in the shared directory.
## SRE Relevance
Use a shared group for deployment directories without granting broad access to all users.
Audit the directory's group and write permissions together; setgid alone is not an access grant.
## Quick Examples
- `chmod g+s /srv/releases` - enable group inheritance on a directory.
- `ls -ld /srv/releases` - inspect the directory mode and group.
## Common Flags
| Flag | Description |
| --- | --- |
| `g+s` | Set the set-group-ID permission bit |
## Related Topics
- [Permissions](permissions.md)
- [`chmod`](chmod.md)
- [Groups](groups.md)
