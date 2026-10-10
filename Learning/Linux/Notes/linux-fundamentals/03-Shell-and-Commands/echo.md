# `echo`

## Overview
`echo` writes its arguments to standard output. Shells often provide it as a built-in; option and escape handling can vary.

## Common Usage
```bash
echo "service check started"
```
This prints a message followed by a newline.

## SRE Relevance
Use `printf` for portable formatting in scripts, especially when data may contain backslashes or option-like text. Avoid printing secrets into logs or terminals.

## Quick Examples
- `echo "$HOME"` prints the home directory.
- `printf '%s\n' "$status"` gives predictable formatting.

## Common Flags
| Flag | Meaning |
| --- | --- |
| `-n` | Omit the trailing newline in many implementations; see [`-n`](echo-n.md). |
| `-e` | Interpret some backslash escapes in many implementations; not portable. |

## Related Topics
- [`-n` (echo option)](echo-n.md)
- [Standard Output](standard-output-stdout.md)
- [Bash](bash.md)
