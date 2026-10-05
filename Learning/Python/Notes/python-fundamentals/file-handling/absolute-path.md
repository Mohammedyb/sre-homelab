# Absolute paths

An absolute path gives the full location of a file, starting from the root of
the drive or file system. It doesn't depend on the folder I'm currently
working in.

On Windows, an absolute path can look like this:

```text
C:\Users\Ada\Documents\notes.txt
```

I can pass an absolute path to `open()` to work with that exact file:

```python
with open(r"C:\Users\Ada\Documents\notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

The `r` before the string makes it a raw string, so backslashes are treated
literally. A [relative path](relative-path.md), such as `"notes.txt"`, is
resolved from the program's current working directory.
