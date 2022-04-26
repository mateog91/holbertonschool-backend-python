#!/usr/bin/env python3

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    result = [
        number async for number in async_generator()
    ]
    return result
