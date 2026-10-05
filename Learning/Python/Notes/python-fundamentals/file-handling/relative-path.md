# Relative paths

A relative path tells Python where a file is in relation to the program's
current working directory. It doesn't include the full drive or file-system
location.

```text
notes.txt
data/notes.txt
```

I can use a relative path with `open()`:

```python
with open("data/notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

The path is resolved from the current working directory, which may not be the
same folder as the Python file. See [absolute paths](absolute-path.md) for
paths that specify a full location.
