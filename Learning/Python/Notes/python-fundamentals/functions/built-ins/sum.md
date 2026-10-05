# `sum()`

`sum()` adds numeric items in an iterable and returns the total.

```python
latencies_ms = [12, 18, 9]
total_ms = sum(latencies_ms)
```

An optional second argument supplies a starting value. For floating-point
measurements where accumulated rounding matters, consider `math.fsum()`.
Do not use `sum()` to concatenate strings.
