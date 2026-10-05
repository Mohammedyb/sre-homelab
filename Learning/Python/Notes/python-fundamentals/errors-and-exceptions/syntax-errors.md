# Syntax errors

## Overview

A syntax error means Python cannot parse the source code, so that code cannot
run. Common causes include a missing colon, unclosed delimiter, or invalid
indentation.

```python
if service_healthy
    print("Service is healthy")
```

Fix the missing colon:

```python
if service_healthy:
    print("Service is healthy")
```

The reported location is where parsing failed; the actual mistake may be
earlier. A syntax error differs from an exception raised while valid code is
running.

## SRE relevance

Run syntax checks, linters, and tests in CI before deploying automation or
services so parse-time failures are caught before execution.
