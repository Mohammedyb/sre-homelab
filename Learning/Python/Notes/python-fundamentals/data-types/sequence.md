# Sequences

## Overview

A sequence is an ordered collection whose items can be accessed by position.
Strings, lists, and tuples are common sequences; indexing starts at `0`.
Lists are mutable, while strings and tuples are immutable.

```python
targets = ("api", "database")
first_target = targets[0]
```

## Common mistakes

Not every iterable is a sequence: sets and dictionaries can be iterated over,
but they are not accessed by numeric index. Choose the collection based on
the required ordering, mutability, and lookup behavior.

See [strings](string.md) and [lists](list.md).
