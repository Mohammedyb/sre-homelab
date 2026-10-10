# GNU GRUB

## Overview
GNU GRUB (GRand Unified Bootloader) is a commonly used boot loader that can select a kernel and pass it startup parameters.
Its menu can offer recovery entries or multiple installed kernels.

## Common Usage
On many Debian-family systems, regenerate the GRUB menu after changing its configuration.
```bash
sudo update-grub
grep -E '^(menuentry|submenu)' /boot/grub/grub.cfg
```
Treat generated `grub.cfg` as output; edit the supported configuration sources instead.

## SRE Relevance
Incorrect boot configuration can make a host inaccessible after restart.
Test kernel and boot changes on a canary and retain console or out-of-band recovery access.

## Quick Examples
The GRUB menu can select an older kernel; `grub-install` installs the boot loader and must target the intended device.

## Common Flags
| Flag | Description |
| --- | --- |
| `grub-install DEVICE` | Install GRUB to a specified boot target; verify the platform and device first |

## Related Topics
- [Boot loader](boot-loader.md)
- [MBR](mbr.md)
- [UEFI](uefi.md)
