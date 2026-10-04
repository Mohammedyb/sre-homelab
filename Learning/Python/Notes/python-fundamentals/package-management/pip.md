# `pip`

I use `pip` to install and manage Python packages. I run it through Python with
`python -m pip` so it uses the `pip` linked to that Python interpreter.

```text
python -m pip install requests
python -m pip show requests
python -m pip list
python -m pip uninstall requests
```

Installing a package and importing it are separate steps. After installing, I
use `import` in my Python code. The import name can differ from the package
name.

I usually install packages in a virtual environment so they stay separate
from other projects.
