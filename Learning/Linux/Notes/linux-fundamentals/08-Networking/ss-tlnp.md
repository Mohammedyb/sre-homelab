# -tlnp (`ss` options)
## Overview
The combined ss options select TCP (-t), listening (-l), numeric endpoints (-n), and process details (-p).

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
sudo ss -tlnp
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: sudo ss -ulnp

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-t` | Include TCP sockets. |
| `-l` | Show listening sockets. |
| `-n` | Use numeric endpoints. |
| `-p` | Show owning processes when permitted. |
## Related Topics
[dns validation](dns-validation.md), [ip addr](ip-addr.md), [ssh](ssh.md)
