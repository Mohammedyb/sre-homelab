# JSON

JSON (JavaScript Object Notation) is a text format for storing and sharing
structured data. It looks similar to Python dictionaries, but JSON is text,
not a Python object.

I use Python's built-in `json` module to convert between JSON and Python
values:

- `json.loads()` parses JSON text into Python values.
- `json.dumps()` converts Python values into JSON text.

```python
import json

json_text = '{"name": "Ada", "age": 36}'
person = json.loads(json_text)

person["age"] = 37
updated_text = json.dumps(person)
```

JSON uses double quotes around strings and object keys. Python's `json` module
also provides `json.load()` and `json.dump()` for reading and writing JSON
files.
