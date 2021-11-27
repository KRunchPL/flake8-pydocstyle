"""
Defines package metadata.
"""
import sys

from flake8_pydocstyle.generic_types import Tuple


if sys.version_info >= (3, 8):  # pragma: no cover (PY38+)
    import importlib.metadata as importlib_metadata
else:  # pragma: no cover (<PY38)
    import importlib_metadata


def _get_versions() -> Tuple[str, str]:
    version = importlib_metadata.version('flake8-pydocstyle')  # type: ignore
    pydocstyle_version = importlib_metadata.version('pydocstyle')  # type: ignore
    return version, pydocstyle_version


version, pydocstyle_version = _get_versions()
