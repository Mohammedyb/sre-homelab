# List `.remove()`

I use `.remove(value)` to remove the first matching value from a list. It
raises `ValueError` if the value is not there.

```python
names = ["Ada", "Grace", "Ada"]
names.remove("Ada")
```

To remove an item by index, I use `.pop(index)` instead.
