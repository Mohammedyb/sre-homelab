# `~` (Home Directory Expansion)
## Overview
In Bash, an unquoted leading `~` expands to the current user's home directory; `~user` may expand to another user's home. Quotes prevent expansion.

## Common Usage
Use interactively for convenience. Scripts needing stable system paths should use explicit locations or a deliberately resolved home variable.

## Bash Example
```bash
printf '%s\n' ~/.*
```

Bash expands `~` and the pattern before `printf`; this may include hidden home-directory entries.

## SRE Relevance
Site reliability engineering (SRE) teams should note: Cron jobs and services may run as different users with different home directories. Never assume the interactive user's home in automation.

## Quick Examples
- Show home: `printf '%s\n' "$HOME"`
- List config: `ls -la ~/.config`

## Common Flags
| Flag or syntax | Meaning |
| --- | --- |
| `~` | Shell expansion syntax, not a command flag; quoted `~` stays literal. |

## Related Topics
[Absolute path](absolute-path.md), [`*` glob](wildcard-asterisk.md), [`?` glob](wildcard-question-mark.md)

