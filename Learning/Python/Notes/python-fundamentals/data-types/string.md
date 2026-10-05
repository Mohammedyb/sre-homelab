# Strings

## Overview

`str` stores Unicode text. Single and double quotes both create strings.
Strings are immutable, so operations produce new strings rather than
changing the original.

```python
service = "api"
message = f"Checking {service}"
```

For dynamic text, f-strings make interpolation clear. Use `join()` to combine
many strings efficiently:

```python
targets = ["api", "worker"]
summary = ", ".join(targets)
```

## Common mistakes

Concatenating values of different types raises `TypeError`; convert values or
use an f-string. Do not build shell commands by interpolating untrusted text;
use argument lists with subprocess APIs instead.

## SRE relevance

Strings carry configuration, log messages, and command output. Normalize and
validate external text at boundaries, and avoid logging secrets.
