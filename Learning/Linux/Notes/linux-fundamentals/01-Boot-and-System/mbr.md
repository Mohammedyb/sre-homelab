# MBR

## Overview
The Master Boot Record (MBR) is a legacy disk layout structure that includes boot code and partition information.
The term also refers to the first sector used by legacy BIOS boot flows.

## Common Usage
Inspect partition layout without modifying disks.
```bash
sudo fdisk -l /dev/sda
lsblk -o NAME,PTTYPE,PARTTYPE,MOUNTPOINTS
```
Confirm the device name carefully; writing boot code to the wrong disk can prevent startup or destroy data.

## SRE Relevance
Legacy partition and boot assumptions matter during migrations, image cloning, and disk recovery.
Record disk layout before changing boot configuration.

## Quick Examples
`PTTYPE` can report `dos` for an MBR-style partition table; modern systems often use GPT instead.

## Common Flags
| Flag | Description |
| --- | --- |
| `fdisk -l` | List partition tables without entering interactive editing |

## Related Topics
- [BIOS](bios.md)
- [Boot loader](boot-loader.md)
- [UEFI](uefi.md)
