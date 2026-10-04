# `random` module

I use Python's `random` module to generate pseudo-random values, such as a
number for a dice roll.

```python
import random

roll = random.randint(1, 6)
```

`randint(a, b)` can return any integer from `a` to `b`, including both ends.
