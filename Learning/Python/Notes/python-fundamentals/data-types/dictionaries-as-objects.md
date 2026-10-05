# Dictionaries as objects

## Overview

A dictionary is useful for a lightweight record with named fields. Keys are
hashable values; unlike a class instance, a dictionary does not enforce a
fixed schema.

```python
service = {
    "name": "api",
    "healthy": True,
    "latency_ms": 42,
}

if service["healthy"]:
    print(service["name"], service["latency_ms"])
```

## Common mistakes

Misspelled or absent keys can raise `KeyError`. Validate data received from
files or APIs rather than assuming its shape.

For behavior, validation, or stable invariants, consider a
[class](../classes/classes.md). For basic key-value storage, see
[dictionaries](dictionary.md).

## SRE relevance

Dictionaries are convenient for JSON payloads and structured log fields, but
validate untrusted or changing external data before using required keys.
