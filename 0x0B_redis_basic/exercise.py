#!/usr/bin/env python3
""" Redis Module """
import redis
import uuid
from typing import Union, Callable


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
    
    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """ def get """
        data = self._redis.get(key)
        return data if not fn else fn(data)

    def get_str(self, key: str):
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str):
        return self.get(key, int)
