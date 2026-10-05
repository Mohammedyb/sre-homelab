# Comparison operators

Comparison operators evaluate to `True` or `False`. Equality (`==`) compares
values; identity (`is`) checks whether two references point to the same
object.

| Operator | Meaning |
| --- | --- |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Use `is None` to test for `None`; do not substitute `is` for value equality.
For floating-point values, prefer a tolerance-based comparison when exact
binary equality is not meaningful.
