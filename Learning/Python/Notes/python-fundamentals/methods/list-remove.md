# The list `.remove()` method

`.remove(value)` removes the first item in a list that is equal to `value`.
It raises `ValueError` if no matching item is found.

```python
names = ["Ada", "Grace", "Ada"]
names.remove("Ada")
# names is now ["Grace", "Ada"]
```

To remove an item by its index, use `.pop(index)` instead; `.remove()` takes a
value, not an index.
