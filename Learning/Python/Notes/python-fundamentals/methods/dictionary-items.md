# Dictionary `items()`

`dict.items()` returns a dynamic view of a dictionary's key-value pairs. It
can be iterated by unpacking each pair:

```python
schedule = {"Ada": "11:00", "Grace": "13:00"}

for service, healthy in {"api": True, "worker": False}.items():
    print(service, healthy)
```

The view reflects changes to its dictionary; do not structurally modify a
dictionary while iterating over its items.
