#!/usr/bin/env python3
""" task 1. Async Comprehensions """
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async_comprehension coroutine """
    return [n async for n in async_generator()]
