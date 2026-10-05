# `readline()`

`readline()` returns the next line from a file, usually including its newline
character. Repeated calls advance through the file.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
```

At end-of-file it returns an empty string. When processing every line, a
`for line in file` loop is generally simpler and avoids loading all lines at
once.
