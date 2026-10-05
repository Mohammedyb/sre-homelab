# Methods

## Overview

A method is a function defined on a class. Calling an instance method through
an object binds that object as the first argument, conventionally named
`self`.

```python
class RetryPolicy:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Policy: {self.name}"


policy = RetryPolicy("api")
print(policy.describe())
```

Methods can use instance state. Keep them cohesive with the class's
responsibility and avoid unexpected side effects.

See [classes](../classes/classes.md).
