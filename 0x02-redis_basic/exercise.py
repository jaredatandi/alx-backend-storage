#!/usr/bin/env python3
"""Write a string to Redis
"""

import redis
import uuid
from functools import wraps
from typing import Union, Callable, List


def count_calls(method: Callable) -> Callable:
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)

        return output
    return wrapper


class Cache:
    """_summary_
    """
    def __init__(self) -> None:
        """_summary_
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """_summary_

        Args:
            data (Union[str, bytes, int, float]): _description_

        Returns:
            str: _description_
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """_summary_

        Returns:
            _type_: _description_
        """
        if self._redis.exists(key):
            data = self._redis.get(key)
            if fn is not None:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> str:
        """_summary_

        Args:
            key (str): _description_

        Returns:
            str: _description_
        """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """_summary_

        Args:
            key (str): _description_

        Returns:
            int: _description_
        """
        return self.get(key, fn=int)

    def replay(self, method_name: str) -> List[str]:
        """_summary_

        Args:
            method_name (str): _description_

        Returns:
            List[str]: _description_
        """
        input_key = method_name + ":inputs"
        output_key = method_name + ":outputs"

        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        replay_history = []
        for i in range(len(inputs)):
            replay_history.append(f"Input: {inputs[i]}, Output: {outputs[i]}")

        return replay_history
