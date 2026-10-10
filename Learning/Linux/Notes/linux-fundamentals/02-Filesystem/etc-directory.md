# Etc (`/etc`)
## Overview
`/etc` contains host-wide configuration, including service settings, account databases, and network configuration.

## Common Usage
Inspect configuration before changing it; preserve ownership and permissions, and back up files. Locations vary by distribution.

## Bash Example
```bash
ls -la /etc; grep -n '^[^#]' /etc/hosts
```

Lists configuration entries and active, non-comment lines in the hosts file.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Configuration drift in `/etc` can change service behavior. Track managed configuration and review changes before restarting services.

## Quick Examples
- Inspect: `less /etc/hosts`
- Check metadata: `stat /etc/hosts`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `ls -a` | Includes hidden entries when listing `/etc`; the directory name is a path, not an option. |

## Related Topics
[Absolute path](absolute-path.md), [`/var/log`](var-log.md), [Files](files.md)

