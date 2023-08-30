#!/usr/bin/env python3
"""
8-make_multiplier.py
defines a function 'make_multiplier'.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function."""
    return lambda x: x * multiplier
