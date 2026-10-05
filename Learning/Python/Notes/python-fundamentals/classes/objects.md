# Objects

## Overview

Every Python value is an object with a type and identity. An instance created
from a user-defined class can carry state in attributes and behavior in
methods.

## Example

```python
class CheckResult:
    def __init__(self, healthy):
        self.healthy = healthy


result = CheckResult(True)
print(result.healthy)
```

`result` is an instance of `CheckResult`; dot notation accesses its
`healthy` attribute.

## Common mistakes

Two variables can refer to the same mutable object. Mutating it through one
reference is visible through the other. Copy mutable data deliberately when
independent state is required.

See [classes](classes.md) for defining a type and
[dictionaries as objects](../data-types/dictionaries-as-objects.md) for a
lightweight alternative for simple records.
