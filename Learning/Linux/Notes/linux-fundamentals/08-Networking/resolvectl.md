# Resolvectl
## Overview
resolvectl inspects and controls systemd-resolved name resolution, including per-link DNS servers and cache state.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
resolvectl status
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: resolvectl query api.example.com

## Common Flags
| Flag | Purpose |
| --- | --- |
| `status` | Show resolver and per-link DNS configuration. |
| `query NAME` | Resolve a name. |
| `flush-caches` | Clear the local DNS cache. |
## Related Topics
[dns validation](dns-validation.md), [ip addr](ip-addr.md), [ssh](ssh.md)
