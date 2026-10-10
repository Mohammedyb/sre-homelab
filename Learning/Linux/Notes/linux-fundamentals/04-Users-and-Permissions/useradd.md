# Sudo Useradd
## Overview
useradd creates a local account; sudo supplies administrator privilege and options set its home and login shell.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo useradd -m -s /bin/bash appuser
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: sudo useradd -m -s /bin/bash appuser

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-m` | Create and populate the home directory. |
| `-s SHELL` | Set the login shell. |
## Related Topics
[permissions](permissions.md), [sudo](sudo.md)
