# `pip`

`pip` installs and manages Python packages. Run it as `python -m pip` to
associate it with the selected Python interpreter.

```text
python -m pip install requests
python -m pip show requests
python -m pip list
python -m pip uninstall requests
```

Installing a package and importing it are separate steps; the import name
may differ from the package name.

## Common mistakes

Install project dependencies in a
[virtual environment](virtual-environments.md), not globally. Record
dependencies in a manifest or lock file so deployments can reproduce the
environment; review and upgrade them deliberately.
