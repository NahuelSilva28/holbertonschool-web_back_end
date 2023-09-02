#!/usr/bin/env python3
"""
1-async_comprehension.py
Defines a coroutine 'async_comprehension'.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension."""
    return [rand_num async for rand_num in async_generator()]
