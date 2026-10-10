# -R
## Overview
-R means recursive for commands such as chown and chgrp, applying changes throughout a tree.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo chown -R appuser:appgroup /srv/app/data
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo chown -R appuser:appgroup /srv/app/data

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-R` | Apply owner/group changes recursively; verify the target first. |
## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
