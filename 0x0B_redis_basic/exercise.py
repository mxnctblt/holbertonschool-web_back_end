#!/usr/bin/env python3
""" Redis Module """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ def count calls """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ def wrapper """
        key_m = method.__qualname__
        self._redis.incr(key_m)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ def call history """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ def wrapper """
        key = method.__qualname__
        input_key = key + ':inputs'
        output_key = key + ':outputs'

        self._redis.rpush(input_key, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(data))
        return data
    return wrapper


def replay(fn: Callable):
    """ def replay """
    store = redis.Redis()
    count_key = fn.__qualname__
    input_key = count_key + ":inputs"
    output_key = count_key + ":outputs"

    count = store.get(count_key).decode("utf-8")
    print("{} was called {} times:".format(count_key, count))
    inputs = store.lrange(input_key, 0, count)
    outputs = store.lrange(output_key, 0, count)

    for input, output in zip(inputs, outputs):
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print("{}(*{}) -> {}".format(count_key, input, output))


class Cache:
    """ Cache Class """
    def __init__(self):
        """ initialization """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ def get """
        data = self._redis.get(key)
        return data if not fn else fn(data)

    def get_str(self, key: str):
        """ def get str """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str):
        """ def get int """
        return self.get(key, int)
