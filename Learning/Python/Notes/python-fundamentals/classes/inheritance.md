# Class inheritance

## Overview

Inheritance lets a subclass reuse or specialize behavior from a base class.
Use it when the subclass can be treated as the base type without surprising
callers.

## Example

```python
class HealthCheck:
    def __init__(self, name):
        self.name = name

    def run(self):
        return {"name": self.name, "ok": True}


class HttpHealthCheck(HealthCheck):
    def __init__(self, name, url):
        super().__init__(name)
        self.url = url
```

`super().__init__()` runs the base-class initialization. The subclass then
adds its own `url` attribute.

## Common mistakes

- Overriding a method with an incompatible signature can break code that
  expects the base-class interface.
- Prefer composition when one object uses another but is not a specialized
  form of it.

## Interview notes

Explain inheritance as code reuse and polymorphism, but discuss the coupling
and testing costs of deep hierarchies.

See [method overriding](method-overriding.md),
[parent classes](parent-class.md), and [child classes](child-class.md).
