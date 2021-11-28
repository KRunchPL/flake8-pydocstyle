[![license](https://img.shields.io/github/license/KRunchPL/flake8-pydocstyle.svg)](https://github.com/KRunchPL/flake8-pydocstyle/blob/master/LICENSE)

[![latest release](https://img.shields.io/github/release/KRunchPL/flake8-pydocstyle.svg)](https://github.com/KRunchPL/flake8-pydocstyle/releases/latest) [![latest release date](https://img.shields.io/github/release-date/KRunchPL/flake8-pydocstyle.svg)](https://github.com/KRunchPL/flake8-pydocstyle/releases)

[![PyPI version](https://img.shields.io/pypi/v/flake8-pydocstyle)](https://pypi.org/project/flake8-pydocstyle/) [![Python](https://img.shields.io/pypi/pyversions/flake8-pydocstyle)](https://pypi.org/project/flake8-pydocstyle/)

# flake8-pydocstyle

Plugin for [`flake8`](https://github.com/PyCQA/flake8) that runs [`pydocstyle`](https://github.com/PyCQA/pydocstyle/) while linting.

It is running `pydocstyle` as it would be run without any parameters in the command line, so it respects all configuration file options that you can set for example in `pyproject.toml`.

## Reason

Maybe you ask a question why just not use [`flake8-docstrings`](https://github.com/PyCQA/flake8-docstrings). In my use-case I wanted to keep the configuration in the `pyproject.toml` file and be able to use everything that `pydocstyle` has to offer in terms of customization. The `flake8-docstrings` is not reading the `pydocstyle` config files, but provides its own options which was insufficient to me.

## Contributing

If you wish to contribute feel free to create an issue or just straight away fork and create PR to this repository. To save your and my time on discussions please provide a good description for them.

## Development

Development documentation can be found [here](README-DEV.md)
