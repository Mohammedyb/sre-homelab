# Custom exceptions

In my division example, `raise Exception("Divisor cannot be 0")` raises the
general `Exception` type with my message. To create a custom exception type, I
define a class that inherits from `Exception`.

```python
class InvalidDivisorError(Exception):
    pass


def remainder_division(a, b):
    if b == 0:
        raise InvalidDivisorError("Divisor cannot be 0")

    result = a // b
    remainder = a % b
    print(a, "/", b, "is", result, "remainder", remainder)

try:
    remainder_division(10, 0)
except InvalidDivisorError as error:
    print(error)
```

The exception class gives this error its own type, and the message explains
what went wrong. I can catch it by type with `except`. If I don't catch it,
the program stops and reports the error.
