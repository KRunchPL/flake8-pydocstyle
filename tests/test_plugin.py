import os
from unittest.mock import MagicMock

import pytest
from munch import Munch
from pydocstyle.config import IllegalConfiguration
from pytest_mock.plugin import MockerFixture

from flake8_pydocstyle import Flake8PydocstylePlugin
from flake8_pydocstyle.plugin import _ConfigurationParserIgnoringSysArgv


@pytest.fixture(scope='function')
def mocked_check(mocker: MockerFixture) -> MagicMock:
    mocker.patch(
        'flake8_pydocstyle.plugin._files_options',
        {
            os.path.abspath('checked_file'): (
                'codes',
                'ignore_decorators',
                'property_decorators',
                'ignore_self_only_init',
            )
        },
    )
    return mocker.patch('flake8_pydocstyle.plugin.check')


def test_init_stores_filename():
    plugin = Flake8PydocstylePlugin(None, 'test_filename', ['test_lines'])  # type: ignore [arg-type]
    assert plugin.filename == os.path.abspath('test_filename')


def test_run_with_not_checked_file(mocked_check: MagicMock):
    plugin = Flake8PydocstylePlugin(None, 'not_checked_file', ['test_lines'])  # type: ignore [arg-type]
    [_ for _ in plugin.run()]
    mocked_check.assert_not_called()


def test_run_with_checked_file(mocked_check: MagicMock):
    plugin = Flake8PydocstylePlugin(None, 'checked_file', ['test_lines'])  # type: ignore [arg-type]
    [_ for _ in plugin.run()]
    mocked_check.assert_called_once_with(
        filenames=(plugin.filename,),
        select='codes',
        ignore_decorators='ignore_decorators',
        property_decorators='property_decorators',
        ignore_self_only_init='ignore_self_only_init',
    )


def test_run_yield_value(mocked_check: MagicMock):
    plugin = Flake8PydocstylePlugin(None, 'checked_file', ['test_lines'])  # type: ignore [arg-type]
    mocked_check.return_value = [
        Munch(line=2020, code='error_code', short_desc='error_desc'),
    ]
    errors = [error for error in plugin.run()]
    assert errors == [
        (2020, 0, 'error_code error_desc', Flake8PydocstylePlugin),
    ]


def test_configuration_parser_ignores_sys_argv(mocker: MockerFixture):
    mocker.patch('sys.argv', ['program_name', '--non-existing-option', 'inputFile'])
    parser = _ConfigurationParserIgnoringSysArgv()
    parser.get_files_options()
    assert parser._arguments == ['.']


def test_configuration_parser_raises_on_wrong_config(mocker: MockerFixture):
    parser = _ConfigurationParserIgnoringSysArgv()
    mocker.patch.object(parser, '_validate_options', return_value=False)
    with pytest.raises(IllegalConfiguration):
        parser.get_files_options()


def test_get_files_options_return_absolute_paths(mocker: MockerFixture):
    parser = _ConfigurationParserIgnoringSysArgv()
    mocker.patch.object(parser, 'get_files_to_check', return_value=[
        ('file_name_1', [], None, None, False),
        ('file_name_2', [], None, None, False),
    ])
    assert parser.get_files_options() == {
        os.path.abspath('file_name_1'): ([], None, None, False),
        os.path.abspath('file_name_2'): ([], None, None, False),
    }


def test_get_files_options_return_correct_options(mocker: MockerFixture):
    parser = _ConfigurationParserIgnoringSysArgv()
    mocker.patch.object(parser, 'get_files_to_check', return_value=[
        ('file_name_1', ['option_1'], ['decorators_1'], {'properties_1'}, False),
        ('file_name_2', ['option_2'], ['decorators_2'], {'properties_2'}, True),
    ])
    assert parser.get_files_options() == {  # type: ignore[comparison-overlap]
        os.path.abspath('file_name_1'): (['option_1'], ['decorators_1'], {'properties_1'}, False),
        os.path.abspath('file_name_2'): (['option_2'], ['decorators_2'], {'properties_2'}, True),
    }


def test_get_files_options_raises_on_too_many_options(mocker: MockerFixture):
    parser = _ConfigurationParserIgnoringSysArgv()
    mocker.patch.object(parser, 'get_files_to_check', return_value=[
        ('file_name_1', ['option_1'], ['decorators_1'], {'properties_1'}, False, 'TOO_MUCH'),
    ])
    with pytest.raises(ValueError):
        parser.get_files_options()
