# Functions

I use a function to group code I want to run when needed. I define one with
`def` and call it by writing its name followed by parentheses.

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Ada")
```

`name` is a parameter; `"Ada"` is the argument passed in. `return` sends a
value back to the code that called the function. If I don't use `return`, the
function returns `None`.
