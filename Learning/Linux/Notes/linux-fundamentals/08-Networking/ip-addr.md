# `ip addr`

## Overview
- `ip addr` displays and configures Internet Protocol (IP) addresses on interfaces.
- It is part of `iproute2`, the standard Linux networking toolset.
## Common Usage
```bash
ip -br addr
ip addr show dev eth0
```
Use the brief view for an overview and the device view to inspect one interface.
## SRE Relevance
- Check for a missing address or interface state before debugging DNS or an application.
- Compare the affected host's address and routes with its network configuration.
- Avoid changing addresses on remote production hosts without console access or rollback.
## Quick Examples
- `ip link show` lists interfaces and their link state.
- `ip route` shows the routing table; `ip addr` alone does not validate reachability.
## Common Flags
| Flag | Description |
| --- | --- |
| `-br` | Brief, one-line-per-interface output |
| `show dev IFACE` | Display details for one interface |
## Related Topics
- [`ss`](ss.md)
- [DNS validation](dns-validation.md)
- [`ping`](ping.md)
