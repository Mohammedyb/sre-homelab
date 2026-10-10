# Wormhole

## Overview
Magic Wormhole is a tool for secure file transfer between computers; it is not a package manager.
It uses a short human-friendly code to rendezvous peers and encrypts transferred data end to end.

## Common Usage
Install it through a trusted distribution or Python packaging workflow, then send a file to a trusted recipient.
```bash
wormhole send ./incident-bundle.tar.gz
wormhole receive
```
Share the generated code through a separate trusted channel and verify the received file before use.

## SRE Relevance
It can help transfer diagnostic bundles when ordinary file-sharing paths are unavailable.
Treat the code as a secret, avoid sending sensitive dumps without approval, and consider data-retention policy.

## Quick Examples
The sender receives a one-time code; the recipient enters it with `wormhole receive`.

## Common Flags
| Flag | Description |
| --- | --- |
| `--text` | Send a text message instead of a file, where supported |

## Related Topics
- [Package manager](package-manager.md)
- [APT](apt.md)
