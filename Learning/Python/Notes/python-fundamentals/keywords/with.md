# `with`

`with` uses a context manager to establish and clean up a resource around a
block. Cleanup runs when the block exits, including when an exception occurs.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

`open()` returns a context manager for the file, and `as file` binds the
opened handle for use inside the block. See [files](../file-handling/files.md).
