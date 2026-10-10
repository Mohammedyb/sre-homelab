# BIOS

## Overview
BIOS (Basic Input/Output System) is legacy firmware that initializes hardware and begins the boot process.
Legacy BIOS commonly boots from disk boot code associated with an MBR.

## Common Usage
Linux exposes indicators for firmware mode, though a running system cannot show every firmware setting.
```bash
if [ -d /sys/firmware/efi ]; then echo UEFI; else echo BIOS-compatible; fi
```
Use the machine console or provider controls to inspect and change firmware boot order.

## SRE Relevance
Firmware mode and boot order affect recovery, disk-image portability, and automated provisioning.
Keep firmware settings consistent across equivalent hosts.

## Quick Examples
An absent `/sys/firmware/efi` typically means the current boot used legacy BIOS-compatible mode.

## Common Flags
Not applicable; BIOS settings are firmware controls, not Linux command flags.

## Related Topics
- [MBR](mbr.md)
- [UEFI](uefi.md)
- [Boot loader](boot-loader.md)
