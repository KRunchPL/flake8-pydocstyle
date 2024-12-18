0.2.5 - 2024-11-23
===================

Maintenance release.

Cleanup of the README file before archiving the project.


0.2.4 - 2024-02-10
===================

Maintenance release.

Updating dev dependencies.
Using ruff and fixing its rules violations.
Reorganizing linters, typing and tests configuration files.
Removing version specific code for not supported Python versions.


0.2.3 - 2023-11-01
===================

Tag release.

Tagging project as compatible with Python 3.12.
Setting minimal Python version to 3.8.1.


0.2.2 - 2022-02-02
===================

Bugfix release.

Fixes [ValueError bug](https://github.com/KRunchPL/flake8-pydocstyle/issues/6), that occurs with `pydocstyle` version (^6.3).


0.2.1 - 2022-01-04
===================

Bugfix release.

Fixes [ValueError bug](https://github.com/KRunchPL/flake8-pydocstyle/issues/3), that occurs with `pydocstyle` version (^6.2).


0.2.0 - 2021-11-28
===================

Initial release.

Runs `pydocstyle` when `flake8` is running.
Runs it as it would be run without any parameters in the command line, so it respects all configuration file options that you can set for example in `pyproject.toml`.

End-to-end tests were done completely manually with latest `pydocstyle` version (6.1.1)
