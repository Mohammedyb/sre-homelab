# Yes

## Overview
`yes` repeatedly writes a string, or `y` by default, to standard output until stopped or its output destination closes.

## Common Usage
```bash
yes | head -n 3
```
`head` consumes three lines and closes the pipe, causing `yes` to stop; this demonstrates output safely without an unbounded terminal stream.

## SRE Relevance
Unbounded output can consume CPU, fill disks, or flood logs. Never direct `yes` to a production prompt or file without strict limits and explicit review.

## Quick Examples
- `yes no | head -n 2` prints two `no` lines.
- `yes 'test' | head -n 10` bounds generated sample output.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | `yes` accepts an optional repeated string; it has no widely portable flags. |

## Related Topics
- [Stress](stress.md)
- [Pipe Character `|`](../03-Shell-and-Commands/pipe-character.md)
- [Standard Output](../03-Shell-and-Commands/standard-output-stdout.md)
