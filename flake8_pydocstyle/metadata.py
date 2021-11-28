"""
Defines package metadata.
"""
import sys

import pydocstyle


name = 'flake8-pydocstyle'
if sys.version_info >= (3, 8):  # pragma: no cover (PY38+)
    import importlib.metadata
    version = importlib.metadata.version(name)
else:  # pragma: no cover (<PY38)
    import importlib_metadata
    version = importlib_metadata.version(name)  # type: ignore


pydocstyle_version = pydocstyle.__version__
