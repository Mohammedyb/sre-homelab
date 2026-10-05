# `read()`

I use `read()` to get the remaining contents of a file as one string. If I pass
a number, it reads up to that many characters instead.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

See [`readline()`](readline.md) to read one line at a time or
[`readlines()`](readlines.md) to get the lines as a list.
