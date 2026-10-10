# `mkdir`
## Overview
`mkdir` creates directories. It fails when a parent is missing unless `-p` is specified.

## Common Usage
Choose an explicit destination and suitable permissions. Avoid creating under system paths without understanding ownership policy.

## Bash Example
```bash
mkdir -m 0750 ./reports
```

Creates `reports` with requested owner read/write/execute and group read/execute permissions, subject to system rules.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Provision directories declaratively and align permissions with service users. Verify effective ownership and mode afterward.

## Quick Examples
- Create nested path: `mkdir -p ./var/archive`
- Check mode: `stat -c '%A %a %n' ./reports`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-m MODE`, `-p` | `-m` sets requested permissions; `-p` creates missing parents and tolerates an existing target. |

## Related Topics
[`-p`](mkdir-parents-option.md), [Directories](directories.md), [Files](files.md)

