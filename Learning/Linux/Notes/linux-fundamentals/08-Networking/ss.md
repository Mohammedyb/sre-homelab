# `ss`
## Overview
ss (socket statistics) inspects Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) inspects listening and established sockets, including protocol, local address, peer, and process when permitted.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo ss -tlnp
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: ss -tan state established

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-t` | Include TCP sockets. |
| `-a` | Show all sockets. |
| `-n` | Use numeric endpoints. |
| `-p` | Show owning processes when permitted. |
## Related Topics
[dns validation](dns-validation.md), [ip addr](ip-addr.md), [ssh](ssh.md)
