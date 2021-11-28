"""
Provides Python version independent generic types.
"""
import sys


if sys.version_info >= (3, 9):  # pragma: no cover (PY39+)
    from builtins import dict as Dict, list as List, tuple as Tuple
    from collections.abc import Generator
    from re import Pattern
elif sys.version_info >= (3, 8):  # pragma: no cover (PY38+)
    from typing import Dict, Generator, List, Pattern, Tuple
else:  # pragma: no cover (<PY38)
    from typing import Dict, Generator, List, Tuple
    from typing.re import Pattern  # type: ignore


__all__ = ['Dict', 'Generator', 'List', 'Pattern', 'Tuple']
