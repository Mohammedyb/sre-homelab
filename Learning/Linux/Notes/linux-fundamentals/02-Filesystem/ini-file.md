# `.ini` Files

## Overview
- `.ini` is a common filename extension for configuration files organized into sections and key-value pairs.
- Programs use these files to separate settings from application code.
- Linux applications may instead use formats such as TOML, YAML, or plain text.
## Common Usage
```bash
grep -nE '^\[|^[[:space:]]*port[[:space:]]*=' /etc/example.ini
```
Shows section headers and port settings without editing the configuration.
## SRE Relevance
- Inspect application settings during deployment and incident response.
- Validate configuration changes before restarting a service.
- Protect files containing credentials with restrictive ownership and permissions.
## Quick Examples
- `less /etc/example.ini` - inspect without modifying.
- `cp example.ini example.ini.bak` - make a backup before an edit.
- `grep -n 'port' example.ini` - locate port-related entries.
## Common Flags
| Flag | Description |
| --- | --- |
| `-n` | With `grep`, include matching line numbers |
| `-E` | With `grep`, enable extended regular expressions |
## Related Topics
- [`/etc`](etc-directory.md)
- [Files](files.md)
- [`cat`](../03-Shell-and-Commands/cat.md)
- [`nano`](../03-Shell-and-Commands/nano.md)

