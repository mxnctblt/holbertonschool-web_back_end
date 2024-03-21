#!/usr/bin/env python3
""" Redis Module """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache Class """
    def __init__(self):
        """ initialization """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key """
        # Generate a unique key
        key = str(uuid.uuid4())
        # Store the data with the unique key
        self._redis.set(key, data)
        return key
