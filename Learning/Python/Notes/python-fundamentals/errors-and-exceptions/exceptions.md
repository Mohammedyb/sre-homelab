# Exceptions

An exception is an error or unusual event that interrupts normal code. I can
handle an exception with `try` and `except` so my program can respond instead
of stopping unexpectedly.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a whole number.")
else:
    print("Your age is", age)
```

I put code that might fail in `try` and handle a specific exception in
`except`. The `else` block runs when the `try` block finishes without an
exception. I can use `finally` for cleanup code that should run either way.
