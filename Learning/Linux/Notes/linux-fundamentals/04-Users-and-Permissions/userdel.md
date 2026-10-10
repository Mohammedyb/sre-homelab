# Sudo Userdel
## Overview
userdel removes a local user account; sudo userdel performs the operation with administrator privilege.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo userdel appuser
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo userdel appuser

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-r` | Remove home directory and mail spool; check backups first. |
## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
