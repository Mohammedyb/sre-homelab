# Wget
## Overview
wget retrieves files or URLs over supported protocols; validate Transport Layer Security (TLS) and destination paths before downloading artifacts.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
wget -O /var/tmp/health.txt https://example.com/health
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), separate name resolution, routing, transport, and application failures; validate from the affected host.

## Quick Examples
Example: wget --spider https://example.com/health

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-O FILE` | Choose output path. |
| `--spider` | Check availability without downloading content. |
| `--timeout=SECONDS` | Set timeout. |
## Related Topics
[dns validation](dns-validation.md), [ip addr](ip-addr.md), [ssh](ssh.md)
