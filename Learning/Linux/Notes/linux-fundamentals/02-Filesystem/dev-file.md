# Dev File (`/dev`)
## Overview
`/dev` exposes device files and pseudo-devices through which programs access kernel devices or interfaces. `/dev/null` is not ordinary storage.

## Common Usage
Inspect with `ls -l`. Writing to a device can have immediate effects; never write to a block device without verifying target and operation.

## Bash Example
```bash
ls -l /dev/null /dev/zero; stat /dev/null
```

Inspects two common pseudo-devices and their file types and permissions.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Device permissions and availability matter for containers, storage, and hardware. Expose only devices required by a workload.

## Quick Examples
- Discard output: `command > /dev/null`
- Read zero bytes: `head -c 16 /dev/zero | od -An -tx1`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `ls -l` | Shows file type and permissions; leading `c` or `b` indicates character or block device. |

## Related Topics
[Root directory](root-directory.md), [Files](files.md), [Kernel modules](kernel-modules.md)

