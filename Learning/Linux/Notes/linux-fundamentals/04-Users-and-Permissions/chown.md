# chown
## Overview
chown changes the owner and optionally group of files or directories; elevated privileges are usually required.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo chown appuser:appgroup /srv/app/data
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo chown appuser:appgroup /srv/app/data

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-R` | Recurse through descendants; inspect the target tree before use. |
## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
