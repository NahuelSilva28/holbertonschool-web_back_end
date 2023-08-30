#!/usr/bin/env python3
"""
9-element_length.py
Defines a function 'element_length'
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculates the lengths of elements"""
    return [(i, len(i)) for i in lst]
