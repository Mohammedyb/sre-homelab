# `KeyError`

I get a `KeyError` when I use square brackets to look up a dictionary key
that doesn't exist.

```python
person = {"name": "Ada"}
print(person["age"])  # Raises KeyError
```

If a missing key is expected, I can use [`.get()`](../methods/dictionary-get.md)
instead. If I need to handle the error, I can catch `KeyError` with `except`.
