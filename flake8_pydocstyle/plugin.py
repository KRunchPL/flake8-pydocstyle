"""
Contains a code for a plugin that runs pydocstyle for the flake8.
"""
import ast
import os
from typing import cast, Optional, Set

from pydocstyle import check
from pydocstyle.config import ConfigurationParser, IllegalConfiguration

from flake8_pydocstyle.generic_types import Dict, Generator, List, Pattern, Tuple
from flake8_pydocstyle.metadata import pydocstyle_version, version


CheckCodesType = List[str]
IgnoreDecoratorsType = List[Pattern[str]]
PropertyDecoratorsType = Set[str]
IgnoreSelfOnlyInitType = bool


class _ConfigurationParserIgnoringSysArgv(ConfigurationParser):  # type: ignore[misc]
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

    def get_files_options(
        self,
    ) -> Dict[
        str,
        Tuple[
            CheckCodesType,
            Optional[IgnoreDecoratorsType],
            Optional[PropertyDecoratorsType],
            IgnoreSelfOnlyInitType,
        ],
    ]:
        self.parse()
        files_options = {}
        for filename, *options in self.get_files_to_check():
            if len(options) != 4:
                raise ValueError(
                    f'`ConfigurationParser.get_files_to_check` yielded {len(options)} for file "{filename}". '
                    f'Expected number of options is: 4. It might be a result of changes in pydocstyle. '
                    f'Try downgrading pydocstyle and report an issue in flake8-pydocstyle repo.'
                )
            files_options[str(os.path.abspath(filename))] = (
                cast(CheckCodesType, options[0]),
                cast(Optional[IgnoreDecoratorsType], options[1]),
                cast(Optional[PropertyDecoratorsType], options[2]),
                cast(IgnoreSelfOnlyInitType, options[3]),
            )
        return files_options


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
        (
            checked_codes,
            ignore_decorators,
            property_decorators,
            ignore_self_only_init,
        ) = _files_options[self.filename]

        for error in check(
            filenames=(self.filename,),
            select=checked_codes,
            ignore_decorators=ignore_decorators,
            property_decorators=property_decorators,
            ignore_self_only_init=ignore_self_only_init,
        ):
            yield (error.line, 0, f'{error.code} {error.short_desc}', Flake8PydocstylePlugin)
