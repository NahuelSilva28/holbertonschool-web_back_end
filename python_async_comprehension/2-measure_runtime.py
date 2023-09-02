#!/usr/bin/env python3
"""
2-measure_runtime.py
Defines a coroutine 'measure_runtime' to measure the total execution time.
"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total execution time for async_comprehension"""
    start_time = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time()
    total_time = end_time - start_time
    return total_time
