# Arithmetic operators

Arithmetic operators perform numeric calculations.

| Operator | Operation | Example |
| --- | --- | --- |
| `+` | Addition | `2 + 3` is `5` |
| `-` | Subtraction | `5 - 2` is `3` |
| `*` | Multiplication | `3 * 2` is `6` |
| `/` | Division | `5 / 2` is `2.5` |
| `%` | Remainder | `5 % 2` is `1` |
| `**` | Exponentiation | `2 ** 3` is `8` |
| `//` | Floor division (rounds down) | `5 // 2` is `2` |

`/` returns a floating-point result, while `//` rounds down toward negative
infinity. `%` returns the remainder. Division by zero raises
[`ZeroDivisionError`](../errors-and-exceptions/zero-division-error.md).

When calculating durations or rates, keep units explicit and guard
denominators that can be zero.
