# The `os` module

## Overview

The `os` module gives Python access to operating-system interfaces such as file paths, environment variables, and process control. It is useful for scripting, automation, and operational tooling.

## Key concepts

- `os.getcwd()` returns the current working directory.
- `os.path.join()` builds paths safely across platforms.
- `os.environ` gives access to environment variables.
- `os.remove()` deletes a file and `os.rename()` moves or renames it.

## Example

```python
import os

current_dir = os.getcwd()
config_path = os.path.join(current_dir, "config", "app.env")
print(config_path)

if "APP_ENV" in os.environ:
    print(os.environ["APP_ENV"])
```

This example prints the active working directory, builds a file path, and reads an environment variable if it exists.

## Common mistakes

- Do not build paths by manually concatenating strings when `os.path.join()` is available.
- Be careful with `os.environ` when handling secrets; avoid logging environment values.
- File operations should handle `FileNotFoundError` and permission errors explicitly.

## SRE relevance

SRE automation often needs to inspect working directories, environment configuration, and file system state. The `os` module is useful for lightweight operational scripts, but it is not a replacement for more structured path and file APIs in larger applications.

## Interview notes

Be ready to explain the difference between `os.path.join()` and simple string concatenation, and why environment variables are often used for runtime configuration.

## Commands / Code

```python
import os

print(os.getcwd())
print(os.path.exists("/var/log"))
print(os.environ.get("HOME"))
```
