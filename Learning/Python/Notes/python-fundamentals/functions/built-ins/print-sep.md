# `print()` `sep` argument

When given multiple values, `print()` separates them with a space by
default. The `sep` argument selects a different separator.

```python
print("2026", "10", "04", sep="-")
```

This prints `2026-10-04`. `sep` only formats output; use a serializer such as
`json.dumps()` when output must follow a data format.
