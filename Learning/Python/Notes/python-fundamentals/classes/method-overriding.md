# Method overriding

## Overview

Overriding is when a subclass defines a method with the same name as an
inherited method. Calls on the subclass use its implementation.

## Example

```python
class HealthCheck:
    def status(self):
        return "unknown"


class HttpHealthCheck(HealthCheck):
    def status(self):
        return "healthy"


check = HttpHealthCheck()
print(check.status())
```

Use `super().status()` inside an override when the subclass should extend the
parent behavior rather than replace it.

## Common mistakes

Keep the method's expected inputs and return contract compatible with the
parent. A changed contract can break callers that use either class
interchangeably.

## Interview notes

Overriding enables runtime polymorphism. Tests should cover both the shared
interface and the subclass-specific behavior.
