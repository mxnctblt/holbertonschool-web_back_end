#!/usr/bin/env python3
""" Redis Module """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ def count calls """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ def wrapper """
        # Generate a key using the qualified name of the method
        key = method.__qualname__
        # Increment the count for the method
        self._redis.incr(key)
        # Call the original method and return its result
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Cache Class """
    def __init__(self):
        """ initialization """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
