# `journalctl`

## Overview
- `journalctl` queries logs collected by `systemd-journald`.
- Filter by unit, boot, priority, or time to reduce noise during an investigation.
## Common Usage
```bash
journalctl -u api.service --since '30 minutes ago' --no-pager
```
Check the service's recent events, then compare timestamps with alerts and deployments.
## SRE Relevance
- Build an incident timeline and confirm whether a restart or recovery changed service behavior.
- Journal access and retention are controlled by host policy; logs may contain sensitive data.
## Quick Examples
- `journalctl -u api.service -f` follows new service events.
- `journalctl -p err -b` shows errors from the current boot.
## Common Flags
| Flag | Description |
| --- | --- |
| `-u UNIT` | Filter entries for a systemd unit |
| `--since TIME` | Set the start of the time range |
| `-b` | Filter to the current boot |
| `--no-pager` | Print output directly for scripts or capture |
## Related Topics
- [Systemd journal](systemd-journald.md)
- [System logs](system-logs.md)
- [`systemctl`](../05-Processes/systemctl.md)
