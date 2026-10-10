# Bash Script

## Overview
A Bash script is a text file containing commands interpreted by Bash. A shebang such as `#!/usr/bin/env bash` identifies the intended interpreter.

## Common Usage
```bash
#!/usr/bin/env bash
set -euo pipefail
printf 'Host: %s\n' "$(hostname)"
```
Save as `health-check.sh`; `set` enables common strict-mode protections, and the example prints the local hostname.

## SRE Relevance
Scripts automate repeatable operational tasks. Review inputs, permissions, error paths, and side effects; test with safe targets before scheduling in production.

## Quick Examples
- `bash -n health-check.sh` checks syntax without execution.
- `bash ./health-check.sh` runs it explicitly with Bash.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | A script has no standard flags; options are defined by its author. |

## Related Topics
- [Bash](../03-Shell-and-Commands/bash.md)
- [Shebang `#!`](../03-Shell-and-Commands/shebang.md)
- [Exit Codes](exit-codes.md)
