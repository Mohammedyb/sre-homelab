# `raise`

I use `raise` to deliberately signal an exception when my code can't continue
normally. I can raise a built-in exception and include a helpful message.

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("The divisor can't be zero.")
    return a / b
```

If I don't catch the exception, it stops the current operation and reports an
error. I can handle it with a matching `except` block; see
[`try` and `except`](try-except.md).

For an example, see [`ZeroDivisionError`](zero-division-error.md).
