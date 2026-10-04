# Scope

Scope is where Python can find a name, such as a variable or function. A name
created inside a function is local to that function.

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

I can't use `message` outside `greet()`. When Python looks up a name, it
checks the local scope first, then enclosing functions, the global scope, and
built-ins.
