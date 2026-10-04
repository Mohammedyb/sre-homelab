# Virtual environments

I use a virtual environment to keep a project's Python packages separate from
other projects. Python's built-in `venv` module creates one in a `.venv`
folder:

```text
python -m venv .venv
```

In PowerShell, I activate it with:

```text
.\.venv\Scripts\Activate.ps1
```

Then I can install packages into that environment:

```text
python -m pip install requests
```

To leave the environment, I run `deactivate`. I usually keep `.venv` out of
version control and record project dependencies separately.
