# `sudo`

## Overview
- Runs a command as root or another user when the policy authorizes it.
- Authentication, authorization, and command auditing are controlled by `sudoers`.
## Common Usage
```bash
sudo -l
sudo systemctl restart api.service
```
Review allowed commands before using elevated privileges.
## SRE Relevance
- Grant narrowly scoped access through `/etc/sudoers.d`; validate edits with `visudo`.
- Avoid broad `NOPASSWD: ALL` rules and verify service health after privileged changes.
## Quick Examples
- `sudo -u api -- id` runs a check as the `api` account.
- `sudo -k` expires cached credentials for the current session.
## Common Flags
| Flag | Description |
| --- | --- |
| `-l` | List commands allowed by policy |
| `-u USER` | Run the command as another user |
| `-n` | Fail rather than prompt for a password |
## Related Topics
- [Authentication](authentication.md)
- [Authorization](authorization.md)
- [Permissions](permissions.md)
