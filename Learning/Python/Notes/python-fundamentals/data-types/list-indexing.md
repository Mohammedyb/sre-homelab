# List indexing

I use an index to get or change one item in a list. Indexes start at `0`, so
the first item is at index `0`. Negative indexes count from the end; `-1` is
the last item.

```python
names = ["Ada", "Grace", "Katherine"]
print(names[0])   # Ada
print(names[-1])  # Katherine

names[1] = "Guido"  # Replace an item
```

An index outside the list's range raises `IndexError`.
