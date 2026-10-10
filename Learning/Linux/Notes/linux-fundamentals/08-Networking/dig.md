# Dig
## Overview
dig queries the Domain Name System (DNS) and exposes response codes, answer records, resolver, and timing for troubleshooting.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
dig api.example.com A
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: dig @1.1.1.1 api.example.com A +noall +answer

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-t TYPE` | Query a record type, such as A or AAAA. |
| `@SERVER` | Query a selected DNS resolver. |
| `+short` | Print compact answer data. |
## Related Topics
[dns validation](dns-validation.md), [ip addr](ip-addr.md), [ssh](ssh.md)
