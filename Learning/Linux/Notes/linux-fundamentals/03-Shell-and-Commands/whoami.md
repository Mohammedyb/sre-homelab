# `whoami`

## Overview
`whoami` prints the effective username of the current process. It is a quick way to identify the account used by the shell.

## Common Usage
```bash
whoami
```
The output might be `deploy`, `root`, or another account name.

## SRE Relevance
Confirm the active identity before privileged operations. `whoami` shows the effective user, while `id` provides numeric IDs and group membership.

## Quick Examples
- `whoami` verifies the current effective account.
- `id` checks user and group IDs before investigating permission issues.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `whoami` has no commonly used portable flags. |

## Related Topics
- [Users](../04-Users-and-Permissions/users.md)
- [Permissions](../04-Users-and-Permissions/permissions.md)
- [Command Line](command-line.md)
