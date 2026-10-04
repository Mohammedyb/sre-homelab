# List slicing

I use a slice to get several items from a list. The stop index is not
included.

```python
names = ["Ada", "Grace", "Katherine", "Guido"]
print(names[1:3])  # ["Grace", "Katherine"]
```

I can leave out the start or stop to take items from the beginning or through
the end:

```python
print(names[:2])  # First two items
print(names[2:])  # From index 2 to the end
```

A slice makes a new list; it doesn't change the original.
