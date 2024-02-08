#!/usr/bin/env python3
""" task 0. Async Generator """
import random
import asyncio


async def async_generator():
    """  asynchronous coroutine  """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)