# Ping
## Overview
ping sends Internet Control Message Protocol (ICMP) echo requests to test basic reachability and round-trip time; firewalls may block replies.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
ping -c 4 192.0.2.10
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: ping -c 4 api.example.com

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-c COUNT` | Stop after the requested echo count. |
| `-W SECONDS` | Set reply timeout where supported. |
## Related Topics
[dns validation](dns-validation.md), [ip addr](ip-addr.md), [ssh](ssh.md)
