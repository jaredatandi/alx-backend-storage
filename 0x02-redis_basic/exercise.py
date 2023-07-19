#!/usr/bin/env python3
"""Write a string to Redis
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        if self._redis.exists(key):
            data = self._redis.get(key)
            if fn is not None:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> str:
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)