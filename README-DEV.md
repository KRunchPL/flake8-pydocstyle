# Developer information

This file contains the most important developer information for the repository.

## Python

Python part of the code shall follow those base guidelines:

* is compatible with Python version >=3.8.1,
* all code shall pass configured static code checks,
* all defined unit test shall pass,
* all code shall be covered by unit tests.

### Library dependencies

Project is using [Poetry](https://python-poetry.org/) to manage dependencies and building packages.

To install Poetry on your system follow the guide here: [Poetry Installation](https://python-poetry.org/docs/#installation)

If you want to have virtualenv created in `.venv` folder in repository root, configure Poetry with following command:

```console
poetry config virtualenvs.in-project true
```

To create a venv and install all dependencies:

```console
poetry install --no-root --sync
```

To add a production dependency:

```console
poetry add <dependency name>
```

To add a development dependency (like one used by tests):

```console
poetry add --group dev <dependency name>
```

To build new package:

```console
poetry build
```

### Unit tests

Unit tests shall be written using pytest and put in the `tests` directory in the repository root. For dependencies handling see [Dependencies section](#library-dependencies).

To run all the unit tests use the `pytest` command without any parameters in the main folder of the repo. This will start all the unit tests from the `tests` package and count coverage for every python file in the project package.

Results will be written to standard output. Coverage can be found in the `.coverage` file and the HTML version of the report will be put in the `coverage-report` directory.

Pytest configuration is in the `pytest.ini` file. Coverage report configuration is in the `.coveragerc` file.

### Static code checkers

Static checkers are being run on the repository by the PR checker, and therefore they shall be executed before submitting PR either locally or automatically when pushing branch to repository.

#### Linter

`ruff` is the linter of choice for this repository. Additionally, `darglint` is used to check docstrings content (arguments, returns, etc.). As `darglint` has limited configuration capabilities when it comes to choosing linted files, `flake8` is used as `darglint`'s wrapper.

To lint all python code use the `ruff .` and `flake8` commands in the main folder of the repo.

Full linting reports from both tools will be written to standard output.

`flake8` and `darglint` configuration is in the `.flake8` file.

`ruff` configuration is in the `ruff.toml` file.

#### Docstrings checks

`pydocstyle` is being run with `flake8`, but since the integration is done with this plugin, to make sure it does not contain errors, `pydocstyle` is also run separately.

To check all python code use the `pydocstyle` command without any parameters in the main folder of the repo.

`pydocstyle` configuration is in the `pyproject.toml` file.

#### Typing checks

`mypy` is the checker of choice for type checking on this repo.

To check all python code use the `mypy` command without any parameters in the main folder of the repo.

`mypy` configuration is in the `mypy.ini` file.

#### Auto formatter

`ruff` is the formatter of choice on this repo.

To format the whole repo code use `ruff format .`. The PR checker is making sure that the whole code is formatted using this command.

`ruff` configuration is in the `ruff.toml` file.
