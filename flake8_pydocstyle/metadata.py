"""
Defines package metadata.
"""
import sys

import pydocstyle


if sys.version_info >= (3, 8):  # pragma: no cover (PY38+)
    import importlib.metadata as importlib_metadata
else:  # pragma: no cover (<PY38)
    import importlib_metadata


name = 'flake8-pydocstyle'
version = importlib_metadata.version(name)
pydocstyle_version = pydocstyle.__version__
