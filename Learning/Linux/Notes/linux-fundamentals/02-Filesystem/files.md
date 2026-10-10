# Files
## Overview
A file is a named filesystem object holding data or representing another type, such as a symbolic link or device. A pathname identifies it.

## Common Usage
Inspect type, size, owner, and permissions before operating. Quote paths that may contain spaces and treat external path input as untrusted.

## Bash Example
```bash
file /etc/hosts; stat /etc/hosts
```

`file` identifies likely content type; `stat` reports filesystem metadata.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Ownership, permissions, and contents affect service reliability. Back up configuration and avoid exposing secrets in terminals or logs.

## Quick Examples
- List metadata: `ls -l -- /etc/hosts`
- Check regular file: `test -f /etc/hosts && echo regular-file`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `--` | Ends option parsing for supporting commands, so dash-leading filenames are treated as paths. |

## Related Topics
[Directories](directories.md), [Absolute path](absolute-path.md), [`touch`](touch.md)

