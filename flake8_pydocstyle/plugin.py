"""
Contains a code for a plugin that runs pydocstyle for the flake8.
"""

import ast
import os
from typing import Optional

from pydocstyle import check
from pydocstyle.config import ConfigurationParser, IllegalConfiguration

from flake8_pydocstyle.generic_types import Dict, Generator, List, Pattern, Tuple
from flake8_pydocstyle.metadata import pydocstyle_version, version


CheckCodesType = List[str]
IgnoreDecoratorsType = List[Pattern[str]]


class _ConfigurationParserIgnoringSysArgv(ConfigurationParser):  # type: ignore
    """
    Class overrides default pydocstyle parsing by ignoring cli options.

    When running inside flake8 we use only options provided in the config files. We need to provide empty
    options list to the parser, so that it does not try to parse flake8 options.
    """

    def parse(self) -> None:
        """
        Parse the configuration.

        :raises IllegalConfiguration: configuration cannot be parsed
        """
        self._options, self._arguments = self._parse_args([])
        self._arguments = self._arguments or ['.']

        if not self._validate_options(self._options):
            raise IllegalConfiguration()

        self._run_conf = self._create_run_config(self._options)

        config = self._create_check_config(self._options, use_defaults=False)
        self._override_by_cli = config

    def get_files_options(self) -> Dict[str, Tuple[CheckCodesType, Optional[IgnoreDecoratorsType]]]:
        self.parse()
        return {
            os.path.abspath(filename): options
            for filename, *options in self.get_files_to_check()
        }


_files_options = _ConfigurationParserIgnoringSysArgv().get_files_options()


class Flake8PydocstylePlugin:
    """
    Flake8 plugin class.

    It is created by flake8 for each of the files it checks and then iterates over `run` generator that
    returns all the errors found in the file.
    """

    name = 'flake8-docstrings'
    version = f'{version}, pydocstyle: {pydocstyle_version}'

    def __init__(self, tree: ast.Module, filename: str, lines: List[str]) -> None:
        self.filename = os.path.abspath(filename)

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        """
        Search for errors in the file and yield them one by one.

        :yield: tuple containing error details (line_number, column, '{code} {summary}', plugin_class)
        """
        if self.filename not in _files_options:
            return
        checked_codes, ignore_decorators = _files_options[self.filename]

        for error in check(
            filenames=(self.filename,),
            select=checked_codes,
            ignore_decorators=ignore_decorators,
        ):
            yield (error.line, 0, f'{error.code} {error.short_desc}', Flake8PydocstylePlugin)
