# `ZeroDivisionError`

I get a `ZeroDivisionError` when I try to divide a number by zero with `/`,
`//`, or `%`.

```python
result = 10 / 0  # Raises ZeroDivisionError
```

I can check the divisor before dividing:

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("The divisor can't be zero.")
    return a / b
```

I can also [handle the exception](try-except.md) if division by zero is a
possible input.
