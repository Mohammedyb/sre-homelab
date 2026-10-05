# Parent classes

A parent class (base class) defines behavior that subclasses inherit. Keep
the base interface small and stable because changes can affect every
subclass.

```python
class Check:
    def __init__(self, name):
        self.name = name

    def run(self):
        raise NotImplementedError
```

`Check` can provide shared state and a method contract for specific checks.
For a formal interface, Python also has abstract base classes.

See [inheritance](inheritance.md) and [child classes](child-class.md).
