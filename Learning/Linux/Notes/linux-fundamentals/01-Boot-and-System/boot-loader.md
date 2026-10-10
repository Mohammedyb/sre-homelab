# Boot Loader

## Overview
A boot loader starts the operating system by locating and loading its kernel and initial environment.
GNU GRUB is a common example; firmware starts the boot loader.

## Common Usage
Check available kernel images and the configured boot mode before troubleshooting startup.
```bash
ls -lh /boot/vmlinuz*
test -d /sys/firmware/efi && echo UEFI || echo BIOS-compatible
```
On a virtual machine, confirm its firmware setting matches the installed boot configuration.

## SRE Relevance
Boot-loader and firmware mismatches can turn a routine reboot into an outage.
Keep boot configuration under change control and verify recovery-console access.

## Quick Examples
Legacy BIOS systems may start a loader from the MBR; UEFI systems launch an EFI application from an EFI System Partition.

## Common Flags
Not applicable; boot-loader options depend on the specific loader and firmware.

## Related Topics
- [GNU GRUB](gnu-grub.md)
- [BIOS](bios.md)
- [UEFI](uefi.md)
