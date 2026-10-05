# `ls`

`ls` is a shell command for listing directory contents, not a Python
function.

```text
ls
ls path/to/folder
```

On Linux and macOS, `ls -a` includes hidden entries. In PowerShell, `ls` is
an alias for `Get-ChildItem`; `Get-ChildItem -Force` includes hidden items.

Use quoting or escape rules appropriate to the shell when a path contains
spaces. For scripts, prefer language APIs over parsing human-oriented `ls`
output.
