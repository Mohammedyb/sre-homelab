# Classes

## Overview

A class defines the attributes and methods shared by its instances. Classes
are useful when related state and behavior belong together; they are not
necessary for every collection of data.

## Example

```python
class CheckResult:
    def __init__(self, service, healthy):
        self.service = service
        self.healthy = healthy

    def status(self):
        return "healthy" if self.healthy else "unhealthy"


result = CheckResult("api", True)
print(result.status())
```

`result` is an instance. Its attributes hold state, and `status()` operates
on that state.

## Common mistakes

- Use `self.attribute` to store state on an instance; a local variable inside
  a method does not become an attribute automatically.
- Keep a class focused. A class that owns unrelated responsibilities is harder
  to test and change.

## SRE relevance

Small classes can model structured results or clients with shared state.
Keep operational code testable by separating external I/O from core logic.

See [`__init__()`](init-method.md), [objects](objects.md),
[methods](../methods/methods.md), and [inheritance](inheritance.md).
