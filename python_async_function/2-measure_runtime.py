#!/usr/bin/env python3
"""
2-measure_runtime.py
Defines a function 'measure_time' to measure the execution time.
"""

import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average execution time for wait_n(n, max_delay)."""
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    return (time() - start_time) / n
