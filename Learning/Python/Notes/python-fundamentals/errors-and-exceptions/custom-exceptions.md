# Custom exceptions

## Overview

A custom exception type distinguishes an application-specific failure from
built-in errors. Define one when callers need to handle that failure
differently; otherwise, a built-in exception with a clear message is usually
sufficient.

```python
class InvalidConfigurationError(ValueError):
    pass


def parse_port(value):
    try:
        port = int(value)
    except ValueError as error:
        raise InvalidConfigurationError("port must be an integer") from error

    if not 1 <= port <= 65535:
        raise InvalidConfigurationError("port must be between 1 and 65535")
    return port


port = parse_port("8080")
```

Subclassing `ValueError` makes the error meaningful to callers expecting
invalid input. `raise ... from error` preserves the original cause.

## Common mistakes

- Avoid inheriting directly from `BaseException`; custom application errors
  should normally inherit from `Exception` or a suitable subclass.
- Do not catch and discard the exception. Log or report actionable context at
  the boundary that can recover.

## SRE relevance

Typed exceptions let automation distinguish invalid configuration from
transient infrastructure failures and choose an appropriate response.
