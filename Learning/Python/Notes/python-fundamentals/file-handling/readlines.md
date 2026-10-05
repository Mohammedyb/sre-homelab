# `readlines()`

I use `readlines()` to read the remaining lines of a file into a list of
strings. Each string usually includes its newline character.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

For a large file, I can loop over the file instead of loading all its lines
into a list.
