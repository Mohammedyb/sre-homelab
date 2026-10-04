# Lists

I use a list (`list`) to keep items in order. Lists can hold different types
of values, including other lists. They can also be changed after I create them.

```python
empty = []
names = ["Ada", "Grace"]
mixed = ["score", 10, True]
nested = [[1, 2], [3, 4]]
```

I can access or change an item by its index, or get part of a list with a
slice:

```python
names[0] = "Katherine"
first_two = names[0:2]
```

- [List indexing](list-indexing.md)
- [List slicing](list-slicing.md)
- [List methods](../methods/list-append.md), including adding and removing items
