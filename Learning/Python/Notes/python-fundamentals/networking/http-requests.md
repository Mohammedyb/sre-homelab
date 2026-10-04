# HTTP requests

I can send HTTP requests from Python to communicate with a web server. For a
basic GET request, I can use `urlopen()` from the built-in
`urllib.request` module:

```python
from urllib.request import urlopen

with urlopen("https://example.com") as response:
    page = response.read()
```

The response body is returned as bytes. For larger projects, I can also use
the third-party `requests` package.
