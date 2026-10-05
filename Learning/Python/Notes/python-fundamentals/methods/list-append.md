# List `append()`

`list.append(value)` adds one item to the end of a list, modifying that list
in place. It returns `None`.

```python
names = ["Ada"]
names.append("Grace")
```

Use `extend(iterable)` to add multiple items individually. Passing a list to
`append()` adds that list as one nested item.
