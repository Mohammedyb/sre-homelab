# List indexing

## Overview

Indexes select one item from a sequence. Python indexes start at `0`;
negative indexes count from the end, with `-1` selecting the last item.

```python
targets = ["api", "worker", "database"]
first_target = targets[0]
last_target = targets[-1]

targets[1] = "scheduler"
```

## Common mistakes

An index outside the valid range raises `IndexError`. Check that a sequence
is non-empty before selecting an item, or handle the exception if its length
is not known.

See [lists](list.md) and [slicing](list-slicing.md).
