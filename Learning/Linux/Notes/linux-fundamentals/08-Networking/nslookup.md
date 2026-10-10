# Nslookup
## Overview
nslookup queries DNS using a configured or specified resolver; use dig or getent when a more detailed or application-like check is needed.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
nslookup api.example.com
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: nslookup api.example.com 1.1.1.1

## Common Flags
| Flag | Purpose |
| --- | --- |
| `SERVER` | Select the resolver to query. |
## Related Topics
[dns validation](dns-validation.md), [ip addr](ip-addr.md), [ssh](ssh.md)
