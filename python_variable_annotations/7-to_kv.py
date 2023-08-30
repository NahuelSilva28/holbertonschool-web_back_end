#!/usr/bin/env python3
"""
7-to_kv.py
Defines a function 'to_kv'
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple with a string and the square of an int or float."""
    return (k, v ** 2)
