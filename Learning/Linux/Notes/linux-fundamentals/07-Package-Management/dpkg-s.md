# `dpkg -s`

## Overview
`-s` is the `dpkg` option that displays status and metadata for a package in the local database.
It helps distinguish an installed package from an unknown or partially configured package.

## Common Usage
Check package version and status during an incident.
```bash
dpkg -s openssh-server
```
If the package is not installed, `dpkg -s` reports that it cannot find the package.

## SRE Relevance
Package state can explain missing binaries, failed updates, or configuration drift.
Compare the reported version with the approved release before changing the host.

## Quick Examples
Look for `Status: install ok installed` to confirm a normally installed package.

## Common Flags
| Flag | Description |
| --- | --- |
| `-s PACKAGE` | `dpkg` option that displays package status and metadata |

## Related Topics
- [`dpkg`](dpkg.md)
- [dpkg `-L`](dpkg-l.md)
