from settings import REDIS
from typing import Union
import redis


class RedisDb:
    expire = REDIS.get("expire", 60 * 5)

    def __init__(self, host, port, password):
        # StrictRedis: Legacy
        self.engine = redis.Redis(
            host=host,
            port=port,
            password=password,
            decode_responses=True,
        )

    def _set(self, key, value=None):
        """
        set redis {key: value} with expire time
        """
        self.engine.set(key, value, ex=self.expire)

    def _get(self, key) -> Union[str, None]:
        """
        get redis {key: value}
        """
        return self.engine.get(key)
