# HTTP requests

## Overview

HTTP requests let a client communicate with a server using methods such as
GET and POST. Python's standard library includes `urllib.request`:

```python
from urllib.request import urlopen

with urlopen("https://example.com", timeout=5) as response:
    page = response.read()
```

The response body is bytes; decode it according to the response encoding
before treating it as text.

## Common mistakes

Set timeouts so a stalled server cannot block a process indefinitely. Handle
HTTP errors and transport errors separately, and do not assume a successful
connection means the response status indicates success.

For higher-level client behavior, see the third-party
[`requests` package](requests.md).

## SRE relevance

Automation making HTTP calls should set bounded timeouts, validate response
status and content, and retry only transient failures with a bounded policy.
