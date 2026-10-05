# `import`

`import` makes names from a module available to the current module. Importing
the module keeps its names qualified and makes their source clear:

```python
import json

payload = json.loads('{"healthy": true}')
```

I can import a specific name when that improves readability:

```python
from pathlib import Path

config_path = Path("config.json")
```

The module name usually matches a `.py` file without its extension. Prefer
specific imports over `from module import *`; avoid import-time side effects
so modules remain safe to reuse.

See [modules](../modules/module.md) and the
[`random` module](../modules/random.md).
