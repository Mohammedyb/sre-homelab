# `input()`

`input()` reads one line from standard input and returns it as a string. It
is appropriate for interactive command-line tools, not unattended services
or scheduled jobs.

```python
raw_timeout = input("Timeout in seconds: ")
try:
    timeout = float(raw_timeout)
except ValueError:
    print("Enter a numeric timeout.")
```

Validate and convert the response before using it. See
[type conversion](type-conversion.md).
