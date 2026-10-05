# `KeyError`

## Overview

`KeyError` is raised when code requests a dictionary key that is not present.

```python
service = {"name": "api"}
print(service["region"])  # Raises KeyError
```

## Handling

If a missing value is expected, use [`.get()`](../methods/dictionary-get.md)
or test membership. If the key is required, allowing `KeyError` to surface
can expose malformed input early.

## SRE relevance

When reading configuration or API responses, validate required fields at the
boundary and report which input is missing rather than silently using an
unsafe default.
