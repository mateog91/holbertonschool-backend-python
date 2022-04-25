#!/usr/bin/env python3
"""Module for task 0"""
import random
import asyncio


async def wait_random(max_delay: float = 10) -> float:
    random_time = random.uniform(0, max_delay)
    await asyncio.sleep(random_time)
    return random_time
