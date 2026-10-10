# Red Hat RPM

## Overview
RPM means RPM Package Manager, the package format and low-level tooling used across Red Hat-family systems.
DNF is the higher-level package manager commonly used to resolve repositories and dependencies.

## Common Usage
Query an installed package and inspect enabled repositories.
```bash
rpm -q openssh-server
dnf repolist
```
Use DNF for normal installation and updates; use RPM queries when checking package ownership or metadata.

## SRE Relevance
Repository and package provenance determine patch availability and supportability.
Keep repository configuration consistent and validate updates before fleet-wide rollout.

## Quick Examples
`sudo dnf install PACKAGE` installs from configured repositories; `rpm -qf /path` identifies the owning package.

## Common Flags
| Flag | Description |
| --- | --- |
| `rpm -q` | Query installed package information |
| `rpm -qf` | Query the package that owns a file |

## Related Topics
- [Package manager](package-manager.md)
- [Debian APT](debian-apt.md)
