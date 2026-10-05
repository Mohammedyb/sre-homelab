# `range()`

`range()` represents an integer sequence, commonly used to repeat an
operation a known number of times. The stop value is excluded.

```python
for number in range(3):
    print(number)  # 0, 1, 2
```

Use `range(start, stop, step)` to set the initial value and increment:

```python
for attempt in range(1, 4):
    print(attempt)
```

The step cannot be zero. A `range` is iterable and does not eagerly allocate
a list of every number.