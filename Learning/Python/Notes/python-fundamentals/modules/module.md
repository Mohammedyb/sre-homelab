# Modules

## Overview

A module is a Python file that provides names such as functions, classes, and
constants. Modules group code for reuse and provide a namespace.

```python
import json

payload = json.loads('{"status": "ok"}')
```

Keep module-level code limited to definitions and lightweight initialization:
it runs when the module is first imported. Avoid performing network calls or
destructive actions during import.

See [`import`](../keywords/import.md) and
[the `random` module](random.md).
