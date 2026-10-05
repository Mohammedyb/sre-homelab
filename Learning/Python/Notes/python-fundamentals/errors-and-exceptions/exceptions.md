# Exceptions

## Overview

An exception signals that an operation failed or could not complete normally.
Python propagates an unhandled exception up the call stack; a handler can
recover, add context, or report the failure.

## Key concepts

- Catch the narrowest exception that supports a useful recovery action.
- Use `else` for work that should happen only when the `try` block succeeds.
- Use `finally` for cleanup that must run whether the operation succeeds or
  fails. Prefer `with` for resources that support context management.

See [`try` and `except`](try-except.md), [`raise`](raise.md), and
[custom exceptions](custom-exceptions.md).

## SRE relevance

Handle failures at system boundaries, preserve useful error context, and
avoid turning a failed operation into a success-shaped result. Retrying is
appropriate only when the failure may be transient and the operation is safe
to repeat.
