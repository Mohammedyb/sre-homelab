# Host
## Overview
A host is a network endpoint identified by an address and often a name; hostname resolution may involve DNS or local configuration.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
getent ahosts api.example.com
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: hostname -f

## Common Flags
| Flag | Purpose |
| --- | --- |
| N/A | No command-specific flags apply. |

## Related Topics
[dns validation](dns-validation.md), [ip addr](ip-addr.md), [ssh](ssh.md)
