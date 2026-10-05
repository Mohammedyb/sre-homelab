# Absolute paths

## Overview

An absolute path identifies a file from the root of a drive or filesystem.
It does not depend on the process's current working directory.

On Windows, an absolute path can look like this:

```text
C:\Users\Ada\Documents\notes.txt
```

I can pass an absolute path to `open()`:

```python
with open(r"C:\Users\Ada\Documents\notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

The `r` prefix makes this a raw string so backslashes are not interpreted as
escape sequences. `pathlib.Path` is another option for building paths
portably.

## Common mistakes

Do not hard-code machine-specific paths into reusable code. Prefer a path
from configuration or build a path relative to a known base directory.
A [relative path](relative-path.md) is resolved from the current working
directory, which may differ from the script's directory.

## SRE relevance

Absolute paths can be useful for fixed system locations, but scripts should
handle missing files and permissions explicitly and avoid assuming every host
has the same directory layout.
