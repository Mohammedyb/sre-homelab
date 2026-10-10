# Usr Directory (`/usr`)
## Overview
`/usr` holds much user-space software: executables, libraries, shared data, and documentation. It is commonly package-managed.

## Common Usage
Use the package manager to modify installed software rather than manually replacing files under `/usr`.

## Bash Example
```bash
ls -ld /usr /usr/bin /usr/lib
```

Inspects common executable and library locations without changing them.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Image-managed `/usr` supports repeatable hosts. Avoid treating it as application state or local configuration.

## Quick Examples
- Find a program: `command -v bash`
- Check a path: `ls -ld /usr/bin`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-d` | Lists the directory entry itself rather than its contents. |

## Related Topics
[`/bin`](bin-directory.md), [`/lib`](library-directories.md), [`/sbin`](sbin-directory.md)

