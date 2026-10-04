# First-class objects

I can use functions like other values: assign them to variables, pass them to
other functions, or return them from a function.

```python
def greet():
    return "Hello"

say_hello = greet
print(say_hello())
```

`say_hello = greet` assigns the function. `say_hello()` calls it.
