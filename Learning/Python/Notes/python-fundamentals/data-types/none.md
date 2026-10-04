# `None`

I use `None` to represent no value. Its type is `NoneType`.

```python
showtime = None

if showtime is None:
    print("No showtime found")
```

I check for `None` with `is None`. For example, `dict.get()` returns `None` if
a key is missing and I don't provide a default value.
