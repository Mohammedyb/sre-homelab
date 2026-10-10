# Modules (Kernel Modules)
## Overview
Kernel modules extend a running Linux kernel, commonly for drivers and filesystem support. They are typically under `/lib/modules/<kernel-release>`.

## Common Usage
Inspect with `lsmod` or `modinfo`. Loading and removing modules changes host behavior and generally requires administrator privileges.

## Bash Example
```bash
uname -r; find /lib/modules/$(uname -r) -maxdepth 1 -type d
```

Prints the running kernel release and checks its module tree; containers may not have this directory.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Kernel/module mismatches can break drivers or storage after upgrades. Validate kernel and module packages together, especially after reboot.

## Quick Examples
- List loaded modules: `lsmod | head`
- Inspect a module: `modinfo ext4`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-maxdepth 1`, `-type d` | Limits `find` to immediate entries and selects directories. |

## Related Topics
[Library directories](library-directories.md), [`/dev`](dev-file.md), [`find`](find.md)

