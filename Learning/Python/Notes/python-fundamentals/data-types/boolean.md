# Booleans

## Overview

`bool` has two values: `True` and `False`. Comparisons and predicates
commonly produce booleans, which control conditional branches.

```python
status_code = 200
service_healthy = status_code == 200
if service_healthy:
    print("Service is responding")
```

Avoid comparing a boolean to `True` or `False` when the value itself can be
used in the condition. Do not confuse truthiness (for example, a non-empty
list) with the `bool` type.

## SRE relevance

Health checks should encode an explicit success condition. A boolean result
alone may be insufficient for diagnosis, so retain useful failure details
alongside it.
