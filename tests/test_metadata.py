from pytest_mock.plugin import MockerFixture

import flake8_pydocstyle
from flake8_pydocstyle.metadata import _get_versions, pydocstyle_version, version


def test_get_versions(mocker: MockerFixture):
    mocker.patch(
        'flake8_pydocstyle.metadata.importlib_metadata.version',
        side_effect=lambda name: f'{name} my_version',
    )
    assert _get_versions() == ('flake8-pydocstyle my_version', 'pydocstyle my_version')


def test_proper_assignment():
    ret_val = _get_versions()
    assert version == ret_val[0]
    assert pydocstyle_version == ret_val[1]
    assert flake8_pydocstyle.__version__ == ret_val[0]
