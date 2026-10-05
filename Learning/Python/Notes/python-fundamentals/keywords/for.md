# `for` loops

Use a `for` loop to process each item from an iterable without manually
managing an index.

```python
for service in ["api", "worker"]:
    print(service)
```

The loop variable receives each item in turn. Iterating over a stream or file
line by line can avoid loading all data into memory.
