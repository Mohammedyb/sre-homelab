# Update (`updatedb`)
## Overview
`updatedb` refreshes the filename database used by many `locate` implementations. It is not a generic system update command.

## Common Usage
Use the distribution's configured mechanism and respect exclusions, privacy policy, resource limits, and required privileges.

## Bash Example
```bash
sudo updatedb
```

Requests rebuilding the locate index; availability and privilege requirements vary by distribution.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Schedule indexing appropriately and exclude sensitive or ephemeral mounts where policy requires. Freshness affects `locate` output.

## Quick Examples
- Search after refresh: `locate 'service.conf'`
- Check live presence: `test -e /etc/service.conf`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `updatedb` | A command that updates the locate index; consult its manual for implementation-specific options. |

## Related Topics
[`locate`](locate.md), [`find`](find.md), [Files](files.md)

