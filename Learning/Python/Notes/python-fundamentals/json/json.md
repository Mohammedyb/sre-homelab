# JSON

## Overview

JSON (JavaScript Object Notation) is a text format for exchanging structured
data. It resembles Python dictionaries, but JSON text and Python objects are
different representations.

## Key concepts

- `json.loads()` parses JSON text into Python values.
- `json.dumps()` converts Python values into JSON text.
- `json.load()` and `json.dump()` read and write JSON through file objects.

```python
import json

payload = '{"service": "api", "healthy": true}'
health = json.loads(payload)

health["healthy"] = False
updated_payload = json.dumps(health)
```

JSON object keys and strings use double quotes; JSON booleans are `true` and
`false`, while Python uses `True` and `False`. Invalid JSON raises
`json.JSONDecodeError`.

## SRE relevance

JSON is common in APIs, configuration, and structured logs. Validate required
fields and types after parsing, and avoid exposing secrets when logging
payloads.

## Interview notes

Be able to distinguish serialization (`dumps`/`dump`) from parsing
(`loads`/`load`) and identify the Python values JSON can represent.
