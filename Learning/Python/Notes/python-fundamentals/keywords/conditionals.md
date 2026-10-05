# Conditionals: `if`, `elif`, and `else`

Conditionals select which branch runs based on a truth value:

- `if` checks the first condition.
- `elif` checks another condition if the earlier one was false.
- `else` runs if none of the conditions were true.

```python
error_rate = 0.02

if error_rate >= 0.05:
    action = "page"
elif error_rate > 0:
    action = "investigate"
else:
    action = "no action"
```

Python uses indentation to define each block. Conditions can use
[comparison](../operators/comparison.md) and
[logical operators](../operators/logical.md).

## Common mistakes

Empty collections, zero, and empty strings are falsey; non-empty values are
truthy. Make conditions explicit when truthiness could obscure the intended
check, especially for optional values and health states.
