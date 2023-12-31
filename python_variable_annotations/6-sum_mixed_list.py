#!/usr/bin/env python3
"""
6-sum_mixed_list.py
Defines a function 'sum_mixed_list'
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of a mixed list of integers and floats."""
    return sum(mxd_lst)
