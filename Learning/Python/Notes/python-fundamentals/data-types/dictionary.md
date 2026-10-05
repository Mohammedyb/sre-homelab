# Dictionaries

## Overview

A dictionary (`dict`) maps unique, hashable keys to values. Lookup is by key,
not position. Dictionaries preserve insertion order in modern Python, but
code should use keys rather than depend on a particular order unless order is
part of the design.

```python
service = {"name": "api", "healthy": True}
print(service["name"])

service["region"] = "east"
service["healthy"] = False
```

Assignment adds a missing key or updates an existing key.

## Common mistakes

A missing key accessed with brackets raises
[`KeyError`](../errors-and-exceptions/keyerror.md). Use
[`.get()`](../methods/dictionary-get.md) only when a missing key is expected;
use brackets when the key is required so invalid data is not hidden.

Use [`.items()`](../methods/dictionary-items.md) to iterate over keys and
values together.

## SRE relevance

Dictionaries commonly represent decoded JSON and structured configuration.
Validate required keys and value types at system boundaries.

See [dictionaries as records](dictionaries-as-objects.md).
