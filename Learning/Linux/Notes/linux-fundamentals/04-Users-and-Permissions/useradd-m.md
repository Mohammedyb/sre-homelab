# -m (`useradd` create home option)
## Overview
-m asks useradd to create the home directory and populate it from the skeleton directory.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo useradd -m appuser
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo useradd -m appuser

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-m` | Create and populate the home directory. |
## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
