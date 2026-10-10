# `-f` (`rm` Force Option)
## Overview
For `rm`, `-f` ignores missing files and suppresses prompts. It does not make deletion recoverable and can hide mistakes.

## Common Usage
Verify the target before using force; do not casually combine it with recursive deletion or broad globs.

## Bash Example
```bash
test -f ./generated.tmp && rm -f -- ./generated.tmp
```

Scopes removal to the expected file after checking existence. Verify path and context before adapting.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Forceful cleanup silently removes the wrong artifact if variables or paths change. Validate variables and constrain cleanup roots.

## Quick Examples
- Preview matches: `printf '%s\n' ./cache/*.tmp`
- Prompt first: `rm -i -- ./generated.tmp`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `-f`, `--` | `-f` suppresses prompts and missing-file errors; `--` protects dash-leading names. Force plus recursion is especially risky. |

## Related Topics
[`rm`](rm.md), [`-r`](recursive-option.md), [`mv`](mv-command.md)

