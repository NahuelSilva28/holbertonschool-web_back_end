#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
Defines an asynchronous routine 'wait_n'.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that spawns multiple wait_random coroutines."""
    espera = [await wait_random(max_delay) for _ in range(n)]
    return sorted(espera)
