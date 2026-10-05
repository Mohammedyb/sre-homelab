# Running Python from the command line

The `python` command starts the interactive interpreter. Enter `exit()` or
send the shell's end-of-input shortcut to leave it.

Run a script by passing its path:

```text
python my_script.py
```

```text
python folder/my_script.py
```

The process's current working directory remains the directory where the
command was launched; it is not automatically changed to the script's
directory. Use the intended virtual environment's interpreter when project
dependencies matter.
