# `dpkg -L`

## Overview
`-L` is the `dpkg` option that lists files installed by a named Debian package.
It queries the local package database; it does not list files from an uninstalled archive.

## Common Usage
Find a package's configuration or executable path while troubleshooting a service.
```bash
dpkg -L nginx | grep -E '/(sbin|etc)/'
```
Check the package name and installation state if the listing is empty or reports an error.

## SRE Relevance
Knowing package ownership helps avoid unmanaged edits and supports reliable recovery.
For a file whose owning package is unknown, use `dpkg -S /path/to/file`.

## Quick Examples
`dpkg -L openssh-server` lists paths recorded for that installed package.

## Common Flags
| Flag | Description |
| --- | --- |
| `-L PACKAGE` | `dpkg` option that lists files installed by PACKAGE |

## Related Topics
- [`dpkg`](dpkg.md)
- [dpkg `-s`](dpkg-s.md)
