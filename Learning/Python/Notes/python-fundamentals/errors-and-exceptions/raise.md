# `raise`

## Overview

Use `raise` to signal that an operation cannot continue under its current
inputs or state. Choose an exception type that describes the failure.

```python
def require_timeout(timeout_seconds):
    if timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be positive")
```

An unhandled exception propagates to the caller. Catch it only where there is
a recovery or reporting action; see [`try` and `except`](try-except.md).

Use a bare `raise` inside an exception handler to re-raise the current
exception without losing its traceback. See
[custom exceptions](custom-exceptions.md) when callers need a distinct error
type.
