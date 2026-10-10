# SCP
## Overview
Secure Copy Protocol (SCP) copies files over SSH; verify destination, permissions, and host key before transferring production data.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
scp ./artifact.tar.gz ops@example.com:/tmp/
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: scp -P 2222 ./artifact.tar.gz ops@example.com:/var/tmp/

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-r` | Copy directories recursively. |
| `-P PORT` | Set SSH port (uppercase). |
| `-i FILE` | Select identity key. |
## Related Topics
[dns validation](dns-validation.md), [ip addr](ip-addr.md), [ssh](ssh.md)
