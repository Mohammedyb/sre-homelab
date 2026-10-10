# Kernel

## Overview
The Linux kernel is the core that manages hardware, memory, processes, filesystems, and system calls.
It is distinct from the user-space tools that make a complete operating system.

## Common Usage
Inspect the running kernel and recent kernel messages with `uname` and `dmesg`.
```bash
uname -r
sudo dmesg --level=err,warn | tail
```
Use the running version and errors to triage a server that failed after a kernel update.

## SRE Relevance
Kernel regressions, resource limits, drivers, and out-of-memory events can affect every workload on a host.
Check logs and maintain a tested fallback kernel before changing production fleets.

## Quick Examples
`uname -a` prints system and kernel details; `journalctl -k -b` shows this boot's kernel journal.

## Common Flags
| Flag | Description |
| --- | --- |
| `uname -r` | Print the kernel release |
| `dmesg --level` | Filter kernel messages by severity |

## Related Topics
- [Boot loader](boot-loader.md)
- [systemd](systemd.md)
