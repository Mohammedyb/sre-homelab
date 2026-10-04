# Dictionary `.get()`

I use `.get(key)` to read a value from a dictionary without raising a
`KeyError` when the key is missing. It returns `None` by default, or a default
value I provide.

```python
person = {"name": "Ada"}

print(person.get("name"))  # Ada
print(person.get("age", 0))  # 0
```
