# chgrp
## Overview
chgrp changes the group owner of files or directories, subject to ownership and privilege rules.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo chgrp deployers /srv/releases/current
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo chgrp deployers /srv/releases/current

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-R` | Change group recursively. |
| `--reference` | Copy the group from another path. |
## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
