# The `requests` package

I can use the third-party `requests` package to send HTTP requests. I install
it with `pip`, then import it in my code.

```text
python -m pip install requests
```

For example, I can send a GET request and read a JSON response:

```python
import requests

response = requests.get("https://api.example.com/items", timeout=10)
response.raise_for_status()
items = response.json()
```

`raise_for_status()` raises an error if the server returns an unsuccessful
status code. The `timeout` sets how long the request waits for a response.
