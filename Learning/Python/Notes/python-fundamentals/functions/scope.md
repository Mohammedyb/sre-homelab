# Scope

## Overview

Scope determines where a name can be accessed. Python resolves local names
before enclosing-function, global, and built-in names (LEGB lookup).

```python
def build_check_name(service):
    prefix = "health"
    return f"{prefix}-{service}"


check_name = build_check_name("api")
```

`prefix` is local to the call and is not available outside the function.

## Common mistakes

Avoid using `global` to share mutable program state; pass dependencies and
values explicitly. A local assignment can shadow a name from an outer scope.

## SRE relevance

Explicit configuration and function parameters make scripts easier to test
and safer to reuse across environments.
