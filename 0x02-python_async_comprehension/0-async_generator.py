#!/usr/bin/env python3
"""Module for Task 0"""

from typing import Iterator
import random
import asyncio


async def async_generator() -> Iterator[float]:
    """
    async_generator The coroutine will loop 10 times, each time asynchronously
    wait 1 second

    Yields:
        Iterator[int]: yield a random number between 0 and 10.
    """
    for i in range(10):
        rand_int = random.uniform(0, 10)
        yield rand_int
        await asyncio.sleep(1)
