# File modes

## Overview

The `mode` argument to `open()` controls whether the file is read, written,
or created. The default is `"r"`.

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("More notes\n")
```

Common text modes:

- `"r"` reads an existing file. It raises an error if the file doesn't exist.
- `"w"` writes to a file, replacing its contents or creating it if needed.
- `"a"` adds to the end of a file, creating it if needed.
- `"x"` creates a new file and raises an error if it already exists.

Add `"b"` for binary data (for example, `"rb"`); add `"+"` for combined read
and write access (for example, `"r+"`).

## Common mistakes

`"w"` truncates an existing file immediately. Use `"a"` to append or `"x"`
when overwriting must be prevented. Specify `encoding="utf-8"` for text files
when consistent decoding matters.

See [files](files.md) for examples.
