#!/usr/bin/env python3
"""Module for task 2"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time measuer elapsed time in seconds

    Args:
        n (int): number of repeats
        max_delay (int): max delay per repeat

    Returns:
        float: total time in seconds
    """
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter() - start
    return float(end)
