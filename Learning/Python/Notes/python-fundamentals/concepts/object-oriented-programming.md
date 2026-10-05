# Object-oriented programming

## Overview

Object-oriented programming (OOP) groups related state and behavior into
objects. It is one way to structure a program, not a requirement for every
problem.

## Example

```python
class ProbeResult:
    def __init__(self, target, latency_ms):
        self.target = target
        self.latency_ms = latency_ms

    def is_slow(self, threshold_ms):
        return self.latency_ms > threshold_ms


result = ProbeResult("api", 120)
print(result.is_slow(100))
```

The class keeps target data and latency-related behavior together.

## Trade-offs

Classes help when state has invariants or several operations. For simple
records or stateless transformations, dictionaries and functions can be
clearer. Avoid classes that add indirection without owning meaningful state
or behavior.

## SRE relevance

OOP can organize reusable clients, health checks, and policy objects. Keep
network and filesystem effects explicit so unit tests can exercise logic
without production dependencies.

See [classes](../classes/classes.md) and
[dictionaries as objects](../data-types/dictionaries-as-objects.md).
