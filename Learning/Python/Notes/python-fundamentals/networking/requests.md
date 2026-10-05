# The `requests` package

## Overview

`requests` is a third-party HTTP client. Install it in the project's
[virtual environment](../package-management/virtual-environments.md):

```text
python -m pip install requests
```

## Example

```python
import requests

response = requests.get("https://api.example.com/health", timeout=(2, 5))
response.raise_for_status()
health = response.json()
```

`raise_for_status()` raises an exception for unsuccessful HTTP status codes.
The connect/read timeout tuple bounds waiting; it is not necessarily a total
request deadline.

## Common mistakes

- Always set a timeout; requests otherwise can wait indefinitely.
- A timeout does not automatically make retrying safe. Consider idempotency,
  retry limits, backoff, and the operation's deadline.
- Check and validate the response before trusting its content.

## SRE relevance

External calls are failure boundaries. Record useful status and latency
context, and avoid logging credentials or sensitive response data.
