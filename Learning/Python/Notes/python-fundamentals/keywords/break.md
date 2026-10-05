# `break`

`break` exits the innermost enclosing loop immediately. Use it when the loop
has found a result or reached a stopping condition.

```python
for number in range(5):
    if number == 3:
        break
    print(number)
```

This prints `0`, `1`, and `2`. In nested loops, `break` exits only the
innermost loop; use a function return or another explicit condition to stop
an outer loop too.