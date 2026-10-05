# `__init__()`

## Overview

Python calls `__init__()` after creating an instance. I use it to establish
the instance's initial state and validate constructor inputs.

## Example

```python
class RetryPolicy:
    def __init__(self, attempts, delay_seconds):
        if attempts < 1:
            raise ValueError("attempts must be at least 1")
        self.attempts = attempts
        self.delay_seconds = delay_seconds


policy = RetryPolicy(attempts=3, delay_seconds=1)
```

`self` refers to the new instance. `__init__()` initializes it; `__new__()`
is responsible for creating it.

## Common mistakes

- Assign constructor values to `self` if they must persist on the instance.
- Do not return a value from `__init__()`; it must return `None`.
- Validate configuration early so invalid state does not propagate into
  runtime operations.

## SRE relevance

Configuration objects can reject invalid retry limits, timeouts, or endpoint
values when they are created, rather than failing later during an incident.
