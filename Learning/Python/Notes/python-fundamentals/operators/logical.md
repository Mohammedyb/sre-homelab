# Logical operators

Logical operators combine or invert conditions. `and` is true when both
operands are truthy, `or` when at least one is truthy, and `not` negates
truthiness.

- `and` is true when both conditions are true.
- `or` is true when at least one condition is true.
- `not` reverses a condition.

```python
if service_healthy and response_time_ms < 500:
    print("Service meets the check")
```

`and` and `or` short-circuit and return one of their operands, not
necessarily a `bool`. Use parentheses for complex conditions to make
precedence clear.
