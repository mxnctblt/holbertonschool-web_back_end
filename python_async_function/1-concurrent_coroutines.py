#!/usr/bin/env python3
""" task 1. Let's execute multiple coroutines at the same time with async """
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ return the list of all the delays """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
