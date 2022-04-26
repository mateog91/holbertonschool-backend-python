#!/usr/bin/env python3
"""Module for task 1"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n wait n number of times

    Args:
        n (int): number of times to repeat
        max_delay (int): max time to wait

    Returns:
        list[float]: _description_
    """
    wait_list = await asyncio.gather(*(task_wait_random(max_delay)
                                       for _ in range(n)))
    wait_list.sort()
    return wait_list
