# `with`

I use `with` to work with a resource and have it cleaned up when the block
ends. For example, it closes a file automatically, even if an error happens
inside the block.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

Here, `open()` provides the file and `as file` gives it a name I can use inside
the indented block. See [files](../file-handling/files.md) for more examples.
