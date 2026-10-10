# Package Manager

## Overview
A package manager installs, upgrades, queries, and removes software using distribution packages and repositories.
It tracks files and dependencies to make host changes more repeatable.

## Common Usage
Use the native package manager for the host's distribution rather than downloading arbitrary binaries.
```bash
cat /etc/os-release
apt policy nginx
```
On a Debian-family server, `apt policy` helps verify the candidate version and repository.

## SRE Relevance
Package sources and versions affect security, reproducibility, and service behavior.
Pin or promote tested versions through managed images and maintenance windows.

## Quick Examples
Debian-family systems use APT; RPM Package Manager (RPM)-based systems commonly use DNF with RPM packages.

## Common Flags
Not applicable; flags depend on the specific package-manager command.

## Related Topics
- [Debian APT](debian-apt.md)
- [Red Hat RPM](red-hat-rpm.md)
- [APT](apt.md)
