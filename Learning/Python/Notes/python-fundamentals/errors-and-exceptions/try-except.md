# `try` and `except`

## Overview

Use `try`/`except` to handle an expected failure at the point where the
program can recover or add useful context. Keep the `try` block narrow.

```python
try:
    timeout = float(input("Timeout in seconds: "))
except ValueError:
    print("Timeout must be a number.")
else:
    if timeout <= 0:
        raise ValueError("Timeout must be positive.")
    print("Using timeout:", timeout)
```

`except` handles matching exceptions; `else` runs only if the `try` block
succeeds. A `finally` block runs during cleanup regardless of success or
failure.

## Common mistakes

- Avoid bare `except:` and broad `except Exception:` unless the boundary has
  a deliberate policy for every failure.
- Do not put unrelated code in `try`; it can cause the handler to catch
  failures from the wrong operation.

## SRE relevance

Translate errors into useful logs or exit statuses at process boundaries.
Preserve the original exception and traceback when re-raising.
