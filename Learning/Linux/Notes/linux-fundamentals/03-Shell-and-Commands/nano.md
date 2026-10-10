# Nano

## Overview
Nano is a terminal text editor designed for straightforward interactive editing. It displays common keyboard shortcuts at the bottom of the screen.

## Common Usage
```bash
nano /etc/hosts
```
Editing protected system files may require authorized elevated access; review changes before saving.

## SRE Relevance
Nano is useful for quick edits over SSH, but production configuration changes should follow review, backup, and change-control practices.

## Quick Examples
- `Ctrl+O` writes the file; `Ctrl+X` exits.
- `nano -v file` opens a file in view-only mode on supported versions.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-B` | Save a backup before writing. |
| `-v` | View file without editing. |

## Related Topics
- [Nano Newfile](nano-newfile.md)
- [Less](less.md)
- [`/etc`](../02-Filesystem/etc-directory.md)
