# `import`

I use `import` to use code from another module. I can import the whole module
and access its contents through the module name:

```python
import random

print(random.randint(1, 6))
```

Or, I can import a specific name from a module:

```python
from employee import Employee

employee = Employee("Ada", "Lovelace")
```

The module name comes from the Python file name without `.py`. For example,
`employee.py` provides the `employee` module. See [modules](../modules/module.md)
and the [`random` module](../modules/random.md).
