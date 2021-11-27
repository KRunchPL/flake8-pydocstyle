# Developer information

This file contains developer information for the repository.

## Python

Python part of the code should follow those base guidelines:
* used Python version is >=3.6.0;
* all the code should pass linting.

### Dependencies

Project us using [Poetry](https://python-poetry.org/) to manage dependencies and building package.

To install Poetry on your system follow the guide here: [Poetry Installation](https://python-poetry.org/docs/#installation)

If you want to have virtualenv created in `.venv` folder in repository root, configure Poetry with following command:
```
poetry config virtualenvs.in-project true
```

To create a venv and install all dependencies run:
```
poetry install
```

For more usage see [Poetry Documentation](https://python-poetry.org/docs/)

### Tests

Tests should be written using pytest and put in the `tests` package. For dependencies handling see [Dependencies section](#dependencies).

To run all the tests use the `pytest` command without any parameters in the main folder of the repo. This will start all the tests from the `tests` package and count coverage for every python file in the `flake8_pydocstyle` package.

Results of tests will be written to standard output. Coverage can be found in the `.coverage` file and the HTML version of the report will be put in `coverage-report` directory.

Pytest configuration is in `pyproject.toml` file.

### Static code checkers

Few static checkers are being run on the repository as PR checker and therefore should be run before submitting PR.

#### Linter

`flake8` with few plugins: `flake8-isort`, `darglint` and the `flake8-pydocstyle` itself.

To lint all python code use the `flake8` command without any parameters in the main folder of the repo.

Full linting report in HTML form will be available in `flake8-report` directory. Summary will be written to standard output.

`flake8` and `darglint` configuration is in the `setup.cfg` file.

`isort` and `pydocstyle` configuration is in the `pyproject.toml` file.

#### Docstrings checks

`pydocstyle` is being run with `flake8`, but since the integration is done with this plugin, to make sure it does not contain errors, `pydocstyle` is also run separately.

To check all python code use the `pydocstyle` command without any parameters in the main folder of the repo.

`pydocstyle` configuration is in the `pyproject.toml` file.

#### Typing checks

`mypy` is the plugin of choice for typing checks on this repo.

To check all python code use the `mypy` command without any parameters in the main folder of the repo.

`mypy` configuration is in the `pyproject.toml` file.
