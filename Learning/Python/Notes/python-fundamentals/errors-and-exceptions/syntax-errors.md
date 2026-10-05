# Syntax errors

A syntax error means Python can't understand how the code is written. It
usually prevents the program from running. Missing a colon or mismatching
quotes or parentheses can cause one.

```python
# Missing a colon after the condition
if age >= 18
    print("Adult")
```

Add the colon to fix it:

```python
if age >= 18:
    print("Adult")
```

The error message points to where Python noticed the problem. The actual
mistake can be on that line or just before it. A syntax error is different
from an exception that happens while valid code is running.
