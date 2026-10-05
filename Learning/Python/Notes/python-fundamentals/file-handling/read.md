# `read()`

`read()` returns the remaining file contents as a string. An optional size
limits how many characters are read.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

Reading without a size loads the entire remaining file into memory. For large
files, read bounded chunks or iterate over lines. See
[`readline()`](readline.md) and [`readlines()`](readlines.md).
