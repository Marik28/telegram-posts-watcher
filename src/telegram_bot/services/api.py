import http

import aiohttp

from telegram_bot.exceptions import ApiException
from telegram_bot.models.vk_objects import WallPost
from telegram_bot.settings import settings


class ApiService:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.vk_api_url = settings.vk_api_url
        self.vk_api_token = settings.vk_api_token
        self.api_version = settings.api_version
        self.groups_to_track = [-152811046]

    async def get_latest_posts(self) -> list[WallPost]:
        """:raises ApiException"""
        posts = []
        for group_id in self.groups_to_track:
            query = {
                "owner_id": group_id,
                "v": self.api_version,
                "count": 100,
                "access_token": self.vk_api_token,
            }
            response = await self.session.get(f"{self.vk_api_url}wall.get/", params=query)
            if response.status == http.HTTPStatus.OK:
                response_json = await response.json()
                posts.extend([WallPost.parse_obj(post) for post in response_json["response"]["items"]])
            else:
                raise ApiException(f"Произошла непредвиденная ошибка.")
        return posts
