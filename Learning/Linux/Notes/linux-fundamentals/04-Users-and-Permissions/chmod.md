# `chmod`

## Overview
- `chmod` changes file or directory permission bits; it does not change ownership.
- Use symbolic modes for a targeted change or octal modes for an exact permission set.
## Common Usage
```bash
chmod 640 /etc/app/app.conf
```
This gives the owner read/write access, the group read access, and others no access.
## SRE Relevance
- Correct permissions resolve service access failures without making files world-writable.
- Check the full path and owning service identity before changing a production file.
## Quick Examples
- `chmod u+x deploy.sh` adds execute permission for the owner.
- `chmod -R o-rwx /srv/app` recursively removes others' access; inspect the target first.
## Common Flags
| Flag | Description |
| --- | --- |
| `-R` | Change permissions recursively; avoid broad paths |
| `-c` | Report each permission change |
## Related Topics
- [Object permissions](object-permissions.md)
- [Octal notation](octal-notation.md)
- [`chown`](chown.md)
