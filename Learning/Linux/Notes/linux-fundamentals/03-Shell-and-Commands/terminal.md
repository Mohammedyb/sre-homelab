# Terminal

## Overview
A terminal is a text interface for interacting with a command-line shell. It is the input/output window; the shell interprets commands.

## Common Usage
Open a terminal session and run commands such as:
```bash
pwd
```
This prints the working directory, helping confirm where commands will run.

## SRE Relevance
Terminals are used for remote administration, incident response, and running tools over SSH. Confirm the host and account before changing production.

## Quick Examples
- `ssh ops@server.example` opens a remote session.
- `exit` closes the current shell session.

## Common Flags
| Flag | Meaning |
| --- | --- |
| N/A | A terminal is an interface, not a command with standard flags. |

## Related Topics
- [Command Line](command-line.md)
- [Shells](shells.md)
- [SSH](../08-Networking/ssh.md)
