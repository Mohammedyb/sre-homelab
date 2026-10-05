# Dictionary `get()`

`dict.get(key, default)` returns the value for a key, or the default if the
key is absent. The default is `None`.

```python
person = {"name": "Ada"}

print(person.get("name"))
print(person.get("age", 0))
```

Use `get()` when an absent key is an expected case. For required fields,
bracket lookup raises `KeyError` and can reveal malformed input instead of
silently substituting a default.
