# Files

A file stores data on a computer so it can still be there after my program
stops. It has a name and a location, called its path. A text file can store
plain text, such as notes or JSON data.

I use `open()` to access a file. It gives me a file object that I can read
from or write to. A [`with` statement](../keywords/with.md) closes the file
for me when I'm done.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

I can read the whole file with [`read()`](read.md), one line with
[`readline()`](readline.md), or the remaining lines as a list with
[`readlines()`](readlines.md).

The mode controls what I do with the file:

- `"r"` reads an existing file.
- `"w"` writes to a file, replacing its contents or creating it if needed.
- `"a"` adds to the end of a file, creating it if needed.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("My notes")

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nMore notes")
```

I can use a path instead of just a file name to work with a file in another
folder. An [absolute path](absolute-path.md) gives the file's full location.
A [relative path](relative-path.md) locates it from the current working
directory.
