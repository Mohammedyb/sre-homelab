# List `remove()`

`list.remove(value)` deletes the first matching value in place. It raises
`ValueError` if the value is absent.

```python
names = ["Ada", "Grace", "Ada"]
names.remove("Ada")
```

To remove an item by index, use `pop(index)`. Check membership first only
when absence is expected; otherwise the exception can expose an unexpected
state.
