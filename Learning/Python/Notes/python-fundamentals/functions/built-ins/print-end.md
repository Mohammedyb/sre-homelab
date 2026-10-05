# `print()` `end` argument

`print()` writes a newline after each call by default. The `end` argument
changes the text written at the end.

```python
print("Hello", end=" ")
print("there")
```

The two calls produce `Hello there` on one line. Avoid suppressing line
breaks in logs unless another component reliably separates records.
