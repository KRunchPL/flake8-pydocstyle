"""
Provides Python version independent generic types.
"""
import sys


if sys.version_info >= (3, 9):  # pragma: no cover (PY39+)
    from builtins import dict as Dict, list as List, tuple as Tuple
    from collections.abc import Generator
    from re import Pattern
else:  # pragma: no cover (PY38+)
    from typing import Dict, Generator, List, Pattern, Tuple


__all__ = ['Dict', 'Generator', 'List', 'Pattern', 'Tuple']
