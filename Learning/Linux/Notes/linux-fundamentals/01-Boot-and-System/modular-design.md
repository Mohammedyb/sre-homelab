# Modular Design

## Overview
Modular design separates system responsibilities into components that can be replaced or configured independently.
Linux supports loadable kernel modules for optional drivers and features.

## Common Usage
Use `lsmod` to inspect loaded modules and `modinfo` to review one before loading it.
```bash
lsmod | head
modinfo e1000e
```
For example, check whether a network driver is present when diagnosing a missing interface.

## SRE Relevance
Modules can add hardware support without rebuilding the kernel, but incorrect or incompatible modules can destabilize hosts.
Validate driver changes on a canary and keep recovery access available.

## Quick Examples
`sudo modprobe MODULE` loads a module; `sudo modprobe -r MODULE` attempts to remove one.

## Common Flags
| Flag | Description |
| --- | --- |
| `modprobe -r` | Remove a module when it is not in use |
| `modinfo -F` | Print a selected module metadata field |

## Related Topics
- [Kernel](kernel.md)
- [Boot loader](boot-loader.md)
