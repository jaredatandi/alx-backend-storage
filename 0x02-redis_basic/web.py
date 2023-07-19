#!/usr/bin/env python3
"""Count url requests

    Returns:
        _type_: _description_
"""

import redis
import requests


def track_url_count(url: str, redis_client: redis.Redis) -> None:
    count_key = f"count:{url}"
    redis_client.incr(count_key)
    redis_client.expire(count_key, 10)


def get_page(url: str) -> str:
    redis_client = redis.Redis()
    response = requests.get(url)
    content = response.text

    track_url_count(url, redis_client)

    return content
