# Kill
## Overview
kill sends a signal to a process; the default is SIGTERM, which requests graceful termination rather than forcing immediate exit.

## Common Usage
Inspect or use the concept with this practical Linux command:

```bash
kill -TERM 1234
```

Verify the target and command result before making production changes.

## SRE Relevance
For Site Reliability Engineering (SRE), correlate state and resource use with service health; prefer supervised, graceful changes and verify recovery.

## Quick Examples
Example: kill -TERM 1234

## Common Flags
| Flag | Purpose |
| --- | --- |
| `-s SIGNAL` | Select a signal; default is SIGTERM. |
| `-l` | List signal names. |
| `-0` | Test existence and permission without sending a signal. |
## Related Topics
[ps](ps.md), [systemctl](systemctl.md), [top](top.md)
