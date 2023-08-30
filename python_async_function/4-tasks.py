#!/usr/bin/env python3
"""
4-tasks.py
Defines a function 'task_wait_n'
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Creates asyncio.Tasks for task_wait_random"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))
