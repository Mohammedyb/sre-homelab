# Lib (Library Directories)
## Overview
`/lib`, `/usr/lib`, and architecture-specific paths contain shared libraries and support files. `/lib` may link into `/usr/lib`.

## Common Usage
Use package-manager tools to install or repair libraries; do not copy arbitrary shared objects into system paths.

## Bash Example
```bash
ls -ld /lib /usr/lib; ldconfig -p | head
```

Inspects library paths and prints a sample of the dynamic-linker cache where `ldconfig` is available.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Missing or incompatible libraries can prevent services starting. Compare packages and runtime images when debugging deployments.

## Quick Examples
- Inspect binary dependencies: `ldd /usr/bin/env`
- Resolve library path: `readlink -f /lib`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `ldconfig -p` | Prints the linker cache; this `-p` is unrelated to `mkdir -p`. |

## Related Topics
[`/usr`](usr-directory.md), [Kernel modules](kernel-modules.md), [Files](files.md)

