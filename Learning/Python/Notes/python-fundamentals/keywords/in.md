# `in`

`in` tests membership in a collection and is also used by `for` loops to
iterate over values.

```python
print("api" in ["api", "worker"])

settings = {"region": "east"}
print("region" in settings)  # Checks dictionary keys
```

Membership behavior depends on the type. For dictionaries, `in` checks keys,
not values.