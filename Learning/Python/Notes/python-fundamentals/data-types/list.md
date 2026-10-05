# Lists

## Overview

A list is an ordered, mutable collection. It can contain values of different
types and can be updated after creation.

```python
pending_checks = ["api", "database"]
pending_checks.append("worker")
```

## Common mistakes

Lists are mutable, so aliases share changes. A list slice is shallow, and
removing a missing value with `.remove()` raises `ValueError`.

## SRE relevance

Lists are useful for ordered work queues and results. For large streams,
process items incrementally rather than accumulating unbounded data in
memory.

See [indexing](list-indexing.md), [slicing](list-slicing.md), and list
methods for [adding](../methods/list-append.md) and
[removing](../methods/list-remove.md) items.
