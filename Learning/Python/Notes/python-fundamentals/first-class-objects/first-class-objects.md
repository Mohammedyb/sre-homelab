# First-class objects

## Overview

Functions are first-class objects in Python: code can assign them to
variables, pass them as arguments, store them in collections, or return them
from other functions.

```python
def is_healthy(status_code):
    return status_code == 200


check = is_healthy
print(check(200))
```

Assigning `is_healthy` passes the function object; `is_healthy(200)` calls
it.

## SRE relevance

Passing callables supports reusable retry, filtering, and callback logic.
Keep callbacks small and document when and with what arguments they run.
