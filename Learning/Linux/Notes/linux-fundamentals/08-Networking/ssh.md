# SSH

## Overview
- Secure Shell (SSH) provides encrypted remote login and command execution.
- Host keys verify server identity; user keys or approved identity systems authenticate clients.
## Common Usage
```bash
ssh -o ConnectTimeout=5 ops@host.example.net 'hostname'
```
Use the expected account and verify the host key before trusting a new server.
## SRE Relevance
- Separate DNS, network reachability, host-key, authentication, and remote-command failures.
- Use managed keys, least-privilege accounts, and audited access; never disable host-key checks to hide a mismatch.
## Quick Examples
- `ssh -vv ops@host.example.net` adds connection diagnostics.
- `ssh -J bastion ops@private-host` connects through a jump host.
## Common Flags
| Flag | Description |
| --- | --- |
| `-i FILE` | Select a private identity key |
| `-p PORT` | Connect to a non-default SSH port |
| `-J HOST` | Use a jump host |
| `-o ConnectTimeout=SECONDS` | Bound connection setup time |
## Related Topics
- [`scp`](scp.md)
- [DNS validation](dns-validation.md)
- [`ip addr`](ip-addr.md)
