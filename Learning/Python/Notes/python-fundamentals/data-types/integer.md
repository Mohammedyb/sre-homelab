# Integers

## Overview

`int` represents whole numbers, such as `-3`, `0`, and `42`. Python integers
can grow beyond fixed-width machine sizes, limited in practice by available
memory.

```python
retry_count = 3
http_status = 503
```

## Common mistakes

Input from `input()` or a text file is a string; convert and validate it
before arithmetic. Integer division with `/` produces a `float`; use `//`
when floor division is intended.

## SRE relevance

Use integers for counts, status codes, and discrete retry limits. Validate
that configured counts are within safe operational bounds.
