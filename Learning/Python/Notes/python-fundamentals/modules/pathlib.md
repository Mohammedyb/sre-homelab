# The `pathlib` module

## Overview

The `pathlib` module provides an object-oriented way to work with filesystem paths. It is cleaner and more readable than string-based path handling, especially when building portable code.

## Key concepts

- `Path` represents a filesystem path.
- `Path("...").exists()` checks whether a path exists.
- `Path("...").read_text()` reads file contents as text.
- `Path("...").write_text()` writes text to a file.
- `Path("...").mkdir()` creates directories.

## Example

```python
from pathlib import Path

log_dir = Path("/var/log/myapp")
log_file = log_dir / "app.log"

if not log_dir.exists():
    log_dir.mkdir(parents=True, exist_ok=True)

log_file.write_text("service started\n", encoding="utf-8")
print(log_file)
```

This creates a directory if it does not exist, then writes a log line to a file in that directory.

## Common mistakes

- `Path` objects are not strings; they are path objects.
- Be explicit about `encoding` when writing or reading text files.
- Do not assume a directory exists unless you check it first.

## SRE relevance

`pathlib` is useful when writing operational automation for log shipping, config management, deployment scripts, and artifact handling. It is easier to reason about than raw string concatenation and helps avoid path bugs across Linux and Windows systems.

## Interview notes

A strong answer is to describe how `pathlib` improves readability and portability. Use `Path` and the `/` operator rather than manual string concatenation. Mention that `Path` is preferred in modern Python code for filesystem work.

## Commands / Code

```python
from pathlib import Path

config = Path("/etc/myapp") / "config.yaml"
print(config.name)
print(config.parent)
print(config.exists())
```
