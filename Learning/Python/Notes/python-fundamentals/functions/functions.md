# Functions

## Overview

A function packages an operation behind a name and parameters. Use `return`
to provide a result; a function without an explicit return value produces
`None`.

```python
def calculate_backoff(attempt, base_seconds):
    return base_seconds * (2 ** attempt)


delay = calculate_backoff(attempt=3, base_seconds=1)
```

`attempt` and `base_seconds` are parameters; the values passed at the call
site are arguments.

## Common mistakes

- Keep a function focused and make inputs and outputs explicit.
- Avoid mutable default arguments; they are created once and reused across
  calls.
- Validate inputs and define behavior for boundary values.

## SRE relevance

Small functions make automation easier to test and reuse. Keep side effects
such as network calls or file writes distinct from calculations where
practical.

See [scope](scope.md).
