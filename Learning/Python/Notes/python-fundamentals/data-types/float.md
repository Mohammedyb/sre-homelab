# Floating-point numbers

## Overview

`float` represents real-number approximations, such as `3.14` or `-0.5`.
Many decimal fractions cannot be represented exactly in binary floating
point.

```python
latency_seconds = 0.125
timeout_seconds = 2.5
```

## Common mistakes

Avoid exact equality checks for calculated floats. Use a tolerance or
`math.isclose()` when approximate comparison is appropriate. For exact
financial or decimal arithmetic, consider `decimal.Decimal`.

## SRE relevance

Floats are useful for durations and measurements. Keep units explicit in
variable names and convert consistently before comparing thresholds.
