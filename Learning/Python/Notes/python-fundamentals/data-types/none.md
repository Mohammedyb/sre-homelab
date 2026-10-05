# `None`

## Overview

`None` is Python's singleton value for "no value" or "not set." Its type is
`NoneType`.

```python
result = None

if result is None:
    print("No result available")
```

Use `is None` to check for it. A function without an explicit `return` also
returns `None`. Do not use `None` to mean several different states if those
states need different handling.

For dictionaries, [`.get()`](../methods/dictionary-get.md) returns `None`
for a missing key unless a default is provided.
