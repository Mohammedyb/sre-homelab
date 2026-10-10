# -r (`userdel` remove-home option)
## Overview
-r with userdel removes the user's home directory and mail spool in addition to the account.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo userdel -r retireduser
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo userdel -r retireduser

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-r` | Remove the home directory and mail spool. |
## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
