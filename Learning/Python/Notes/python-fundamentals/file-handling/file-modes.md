# File modes

The `mode` argument in `open()` tells Python what I want to do with a file.
If I leave it out, Python opens the file in read mode (`"r"`).

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("More notes\n")
```

Common modes:

- `"r"` reads an existing file. It raises an error if the file doesn't exist.
- `"w"` writes to a file, replacing its contents or creating it if needed.
- `"a"` adds to the end of a file, creating it if needed.
- `"x"` creates a new file and raises an error if it already exists.

See [files](files.md) for examples of opening and using files.
