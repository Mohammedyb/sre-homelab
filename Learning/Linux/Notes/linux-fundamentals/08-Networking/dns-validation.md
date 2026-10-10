# DNS Validation Workflow
## Overview
DNS means Domain Name System, which maps names to records such as IPv4 A and IPv6 AAAA addresses; resolution can differ across caches and networks.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
resolvectl status; dig api.example.com A; dig api.example.com AAAA
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: getent ahosts api.example.com; curl -v --connect-timeout 3 https://api.example.com/

## Common Flags
| Flag | Purpose |
| --- | --- |
| `dig -t TYPE` | Query record type, e.g. A or AAAA. |
| `dig @SERVER` | Compare a specific resolver. |
| `getent ahosts` | Check resolution through the host name service. |
## Related Topics
[ip addr](ip-addr.md), [ssh](ssh.md)
