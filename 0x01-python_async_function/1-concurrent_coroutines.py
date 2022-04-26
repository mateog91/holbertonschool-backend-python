#!/usr/bin/env python3
"""Module for task 1"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n wait n number of times

    Args:
        n (int): number of times to repeat
        max_delay (int): max time to wait

    Returns:
        list[float]: _description_
    """
    wait_list = await asyncio.gather(*(wait_random(max_delay)
                                       for _ in range(n)))
    wait_list.sort()
    return wait_list
