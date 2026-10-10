# Sticky Bit
## Overview
The sticky bit on a shared directory restricts deletion or renaming of entries to their owner, directory owner, or privileged user.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ls -ld /tmp
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), validate access as the relevant service identity, preserve least privilege, and verify changes with auditable checks.

## Quick Examples
Example: ls -ld /tmp

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[permissions](permissions.md), [useradd](useradd.md), [sudo](sudo.md)
