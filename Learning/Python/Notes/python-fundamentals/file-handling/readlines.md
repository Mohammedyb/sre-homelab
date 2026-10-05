# `readlines()`

`readlines()` returns the remaining file contents as a list of lines. Each
string usually includes its newline character.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

This loads every remaining line into memory, so avoid it for large or
unbounded files. Iterate over the file object to process lines incrementally.
