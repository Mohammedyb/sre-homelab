# `touch`
## Overview
`touch` creates an empty file if absent, or updates timestamps on an existing file by default. It does not truncate existing contents.

## Common Usage
Use for placeholders or timestamp updates. Check targets: changed modification times can affect builds and monitoring.

## Bash Example
```bash
touch ./healthcheck.marker; stat ./healthcheck.marker
```

Creates a marker in the current directory if absent, then reports its metadata.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Marker files can coordinate simple checks, but stale markers may mislead automation. Use explicit state management for critical workflows.

## Quick Examples
- Set a timestamp: `touch -d '2026-01-01T00:00:00Z' file`
- Create only if absent: `touch -- file`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-d DATE`, `--` | Sets a date-derived timestamp; `--` ends option parsing. |

## Related Topics
[Files](files.md), [`mkdir`](mkdir.md), [Absolute path](absolute-path.md)

