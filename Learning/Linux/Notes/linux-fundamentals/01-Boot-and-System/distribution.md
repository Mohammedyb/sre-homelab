# Distribution

## Overview
A Linux distribution combines the Linux kernel with user-space tools, libraries, a package manager, and release policies.
Examples include Debian, Ubuntu, Fedora, and Red Hat Enterprise Linux (RHEL).

## Common Usage
Identify a host's distribution before applying package or service instructions.
```bash
cat /etc/os-release
uname -r
```
This distinguishes, for example, an Ubuntu host using APT from a RHEL host using RPM-based tooling.

## SRE Relevance
Release lifecycle, security support, package versions, and defaults vary by distribution.
Standardize supported images and test automation against every supported family.

## Quick Examples
Use `cat /etc/os-release` for distribution identity and `hostnamectl` for host and operating-system details.

## Common Flags
Not applicable; distribution identity is not a command option.

## Related Topics
- [Debian APT](../07-Package-Management/debian-apt.md)
- [Red Hat RPM](../07-Package-Management/red-hat-rpm.md)
