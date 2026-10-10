# Snaps

## Overview
Snap is a software packaging and distribution system; a snap is an application bundle managed by `snapd`.
It is separate from traditional Debian packages managed by APT.

## Common Usage
Inspect installed snaps and their revisions before managing a snap-based service.
```bash
snap list
snap info lxd
```
Use the publisher, channel, and confinement details to verify that a snap meets production policy.

## SRE Relevance
Snap channels and automatic refresh behavior affect rollout timing and reproducibility.
Set an intentional update policy and test application health after refreshes.

## Quick Examples
`sudo snap refresh PACKAGE` refreshes a snap; `snap changes` shows recent operations.

## Common Flags
| Flag | Description |
| --- | --- |
| `--channel` | Select a snap track/risk/branch channel when supported |
| `--classic` | Request classic confinement when installing a snap that supports it |

## Related Topics
- [Package manager](package-manager.md)
- [APT](apt.md)
