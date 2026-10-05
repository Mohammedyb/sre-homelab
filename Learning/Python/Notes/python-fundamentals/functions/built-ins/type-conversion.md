# Type conversion

Functions such as `int()`, `float()`, and `str()` convert values between
types. Conversions can fail when the input is malformed or incompatible.

```python
port = int("8080")
timeout_seconds = float("2.5")
```

`int(10.6)` truncates toward zero; it does not round to the nearest integer.
Catch `ValueError` when parsing external input and validate allowed ranges
before using the result.

## SRE relevance

Configuration, command-line input, and API payloads often arrive as text.
Convert and validate at the boundary, and report invalid values clearly.
