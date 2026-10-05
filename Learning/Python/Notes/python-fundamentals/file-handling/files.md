# Files

## Overview

A file stores data beyond the lifetime of a process. `open()` returns a file
object used to read or write data; the path identifies where the file is.

Use a [`with` statement](../keywords/with.md) so the file is closed even if
an exception occurs:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

Use [`read()`](read.md) for the remaining contents, [`readline()`](readline.md)
for one line, or [`readlines()`](readlines.md) for a list of remaining lines.
For large files, iterate over the file object to process one line at a time.

The mode controls what I do with the file. See [file modes](file-modes.md)
for the common options.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("My notes")

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nMore notes")
```

## Common mistakes

- `"w"` replaces existing contents; confirm the mode before opening.
- Text files should use an explicit encoding such as UTF-8.
- A relative path uses the process's working directory, not necessarily the
  directory containing the script.

See [file modes](file-modes.md), [absolute paths](absolute-path.md), and
[relative paths](relative-path.md).

## SRE relevance

Use bounded or streaming reads for large logs and data files. Handle missing
files, permission errors, and partial writes explicitly in automation.
