# The `shutil` module

## Overview

The `shutil` module provides file and directory utilities such as copying, moving, removing directories, and working with archive files. It is built for filesystem automation and operational scripts.

## Key concepts

- `shutil.copy2()` copies a file while preserving metadata.
- `shutil.copytree()` copies a directory tree.
- `shutil.rmtree()` removes a directory tree.
- `shutil.move()` moves a file or directory.

## Example

```python
import shutil
from pathlib import Path

source = Path("/tmp/app.log")
backup = Path("/tmp/app.log.bak")

shutil.copy2(source, backup)
print(f"Copied {source} to {backup}")
```

This copies the file and keeps its metadata, which is useful when preserving timestamps or permissions matters.

## Common mistakes

- `shutil.rmtree()` deletes directories recursively; use it carefully.
- Copying and moving files should handle `FileNotFoundError` and permission errors.
- Use explicit target paths rather than relying on working-directory assumptions.

## SRE relevance

SRE and platform automation often need to archive logs, copy artifacts, or move configuration between directories. `shutil` is useful for those workflows, but destructive operations should be gated behind validation and careful logging.

## Interview notes

Be able to distinguish between shallow and metadata-preserving copies. `copy2()` is safer when preserving timestamps and mode bits matters, while `copy()` is lighter and less detailed.

## Commands / Code

```python
import shutil

shutil.copy2("/var/log/app.log", "/tmp/app.log.backup")
shutil.move("/tmp/app.log.backup", "/var/backups/")
```
