# Dictionaries

I use a dictionary (`dict`) to store values as key-value pairs. I look up a
value by its key instead of its position.

```python
person = {"name": "Ada", "age": 36}
print(person["name"])  # Ada

person["language"] = "Python"  # Add a new key-value pair
person["age"] = 37  # Update a value
```

Each key in a dictionary must be unique.

I can use [`.get()`](../methods/dictionary-get.md) to look up a key without
getting an error if it is missing.
Looking up a missing key with square brackets raises a
[`KeyError`](../errors-and-exceptions/keyerror.md).

I can use [`.items()`](../methods/dictionary-items.md) to loop through the
keys and values together.

I can also use dictionaries to [represent objects](dictionaries-as-objects.md)
by storing each object's details as key-value pairs.
