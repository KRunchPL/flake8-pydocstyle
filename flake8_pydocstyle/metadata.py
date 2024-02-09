"""
Defines package metadata.
"""

import importlib.metadata as importlib_metadata

from flake8_pydocstyle.generic_types import Tuple


def _get_versions() -> Tuple[str, str]:
    version = importlib_metadata.version('flake8-pydocstyle')
    pydocstyle_version = importlib_metadata.version('pydocstyle')
    return version, pydocstyle_version


version, pydocstyle_version = _get_versions()
