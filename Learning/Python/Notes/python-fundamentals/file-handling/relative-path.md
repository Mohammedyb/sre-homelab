# Relative paths

## Overview

A relative path is resolved from the process's current working directory. It
does not identify a file independently of where the program was launched.

```text
notes.txt
data/notes.txt
```

I can pass a relative path to `open()`:

```python
with open("data/notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

The working directory may not be the same folder as the script. For a path
relative to the script itself, build it from `Path(__file__).parent`. See
[absolute paths](absolute-path.md) for full file locations.

## Common mistakes

Assuming a relative path starts beside the script can cause failures when a
job runs under a scheduler, service manager, or different shell directory.
Log or explicitly configure the base directory when it matters.
