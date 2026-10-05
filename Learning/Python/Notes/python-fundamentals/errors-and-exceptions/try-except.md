# `try` and `except`

I use a `try`/`except` block to handle an exception that might happen while
my code runs. I put the risky code in `try` and handle a specific exception
in `except`.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a whole number.")
else:
    print("Your age is", age)
```

`except` runs only if the matching exception occurs. `else` runs if the `try`
block succeeds. I catch specific exceptions so I don't hide unrelated errors.
