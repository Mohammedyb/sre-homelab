# `readline()`

I use `readline()` to read the next line from a file. The returned string
usually includes the line's newline character.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
```

Calling it again reads the next line. At the end of the file, it returns an
empty string.
