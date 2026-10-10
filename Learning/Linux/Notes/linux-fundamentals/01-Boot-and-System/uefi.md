# UEFI

## Overview
UEFI (Unified Extensible Firmware Interface) is modern firmware that can launch EFI applications from an EFI System Partition (ESP).
It commonly works with a GUID Partition Table (GPT), though the concepts are not inseparable.

## Common Usage
Check whether the running Linux installation booted in UEFI mode.
```bash
test -d /sys/firmware/efi && echo 'Booted with UEFI' || echo 'Not booted with UEFI'
sudo efibootmgr -v
```
Use `efibootmgr` only when available and with a recovery plan before changing boot entries.

## SRE Relevance
UEFI boot entries, Secure Boot policy, and ESP contents affect host restart and image deployment.
Back up boot configuration and validate changes on a non-critical system first.

## Quick Examples
`efibootmgr -v` displays firmware boot entries; a VM's configured firmware must match its installed boot path.

## Common Flags
| Flag | Description |
| --- | --- |
| `efibootmgr -v` | Show detailed UEFI boot entries |

## Related Topics
- [BIOS](bios.md)
- [Boot loader](boot-loader.md)
- [GNU GRUB](gnu-grub.md)
