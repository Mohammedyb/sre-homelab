# Virtual environments

## Overview

A virtual environment isolates a project's installed packages from other
Python projects. `venv` creates an environment in `.venv`:

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

Deactivate it with `deactivate`. Do not commit the environment directory;
record dependencies and recreate the environment during setup or deployment.

## Common mistakes

Activation changes which `python` and `pip` commands the shell resolves.
When in doubt, use `python -m pip` with the intended interpreter and verify
that the environment's Python is being used.

## SRE relevance

Reproducible environments reduce drift between developer, CI, and runtime
systems. Pin or lock dependencies according to the project's deployment
process.
