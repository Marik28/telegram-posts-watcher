from aioredis import Redis

redis: Redis = await Redis(decode_responses=True)


class RedisService:
    def __init__(self):
        self.redis = redis
        self.links_list = "photo_links"

    async def add_links(self, links: list[str]):
        await self.redis.rpush(self.links_list, *links)
