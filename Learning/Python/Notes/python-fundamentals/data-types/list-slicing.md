# List slicing

## Overview

Slicing selects a range of items. The start index is included and the stop
index is excluded; the optional third value is the step.

```python
services = ["api", "worker", "database", "cache"]
print(services[1:3])
print(services[::2])
```

I can omit the start or stop to slice from the beginning or through the end:

```python
print(services[:2])
print(services[2:])
```

## Common mistakes

A slice creates a new list, so changing it does not change the original
list's top-level items. It is a shallow copy: nested mutable objects remain
shared.
