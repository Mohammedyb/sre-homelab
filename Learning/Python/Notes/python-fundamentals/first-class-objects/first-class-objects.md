# First-class objects

In Python, functions are first-class objects. This means a function can be
assigned to a variable, passed to another function, or returned from a
function, just like other values.

```python
def greet():
    return "Hello"

say_hello = greet
print(say_hello())
```

Assigning `greet` to `say_hello` does not call it; the parentheses in
`say_hello()` call the function.
