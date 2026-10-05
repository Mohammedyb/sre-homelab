# `ZeroDivisionError`

## Overview

Python raises `ZeroDivisionError` when a numeric operation divides by zero,
including `/`, `//`, and `%`.

```python
result = 10 / 0
```

If zero is a valid input but the operation is not defined, handle the case
explicitly:

```python
def utilization(used, capacity):
    if capacity == 0:
        return None
    return used / capacity
```

Returning `None` is appropriate only if callers understand and handle that
meaning. See [`try` and `except`](try-except.md) for exception handling.

## SRE relevance

Guard calculations such as utilization and rates against zero denominators,
and define what the metric should mean when there is no capacity or no
observations.
