# `random` module

Python's `random` module generates pseudo-random values. It is useful for
simulation and non-security-sensitive sampling.

```python
import random

roll = random.randint(1, 6)
```

`randint(a, b)` includes both endpoints. Do not use `random` for tokens,
passwords, or security decisions; use `secrets` for security-sensitive
randomness.
