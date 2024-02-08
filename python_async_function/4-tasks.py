#!/usr/bin/env python3
""" task 4. Tasks """
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ return the list of all the delays """
    delays = []
    tasks = [task_wait_random(max_delay) for i in range(n)]

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
