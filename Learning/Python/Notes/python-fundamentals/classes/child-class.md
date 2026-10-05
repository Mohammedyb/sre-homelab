# Child classes

## Overview

A child class (subclass) inherits behavior from a parent class (base class).
It can add behavior or specialize a method, but inheritance is best used for
a genuine "is a" relationship.

## Example

```python
class HealthCheck:
    def run(self):
        return {"ok": True}


class HttpHealthCheck(HealthCheck):
    def __init__(self, url):
        self.url = url
```

`HttpHealthCheck` inherits `run()` and can add HTTP-specific behavior.

## Common mistakes

- A child class inherits methods, not automatically initialized instance
  attributes. Call the parent's `__init__()` when the parent needs setup.
- Avoid deep inheritance trees; composition is often simpler when components
  merely work together.

See [parent classes](parent-class.md), [inheritance](inheritance.md), and
[method overriding](method-overriding.md).
