import aiohttp
from aiogram import Bot, Dispatcher, types

from .database import Session
from .exceptions import AlreadySubscribedError
from .services.api import ApiService
from .services.users import UsersService
from .settings import settings

bot = Bot(token=settings.telegram_api_token)
dp = Dispatcher(bot)


# async def check_posts_and_send_messages(sleep_for: int):
#     while True:
#         await asyncio.sleep(sleep_for)
#         with Session() as db_session:
#             posts_service = PostsService(db_session)
#             async with aiohttp.ClientSession() as session:
#                 api_service = ApiService(session)
#                 latest_posts = await api_service.get_latest_posts()
#             new_posts = posts_service.filter_new_posts(latest_posts)
#             posts_service.add_posts(new_posts)
#             all_photos_links = []
#             for post in new_posts:
#                 attachments = post.attachments or []
#                 photos = [attachment.photo for attachment in attachments if attachment.photo is not None]
#
#                 for photo in photos:
#                     best_quality_photos_urls = [size.url for size in photo.sizes if size.type == SizeType.W]
#                     all_photos_links.extend(best_quality_photos_urls)
#
#             users_service = UsersService(db_session)
#             users = users_service.get_users()
#
#         for user in users:
#             for link in all_photos_links:
#                 await bot.send_message(user.id, link)

async def get_new_posts(sleep_for: int):
    ...


async def send_message(sleep_for: int):
    ...


@dp.message_handler(commands=["subscribe"])
async def process_subscribe_command(message: types.Message):
    with Session() as session:
        user = message.from_user
        service = UsersService(session)
        try:
            service.add_user(user)
        except AlreadySubscribedError as e:
            msg = str(e)
        else:
            msg = "Вы успешно подписаны на рассылку"

    await message.answer(msg)


@dp.message_handler(commands=["unsubscribe"])
async def process_unsubscribe_command(message: types.Message):
    with Session() as session:
        service = UsersService(session)
        service.delete_user(message.from_user)
        await message.answer("Вы успешно отписались от рассылки")


@dp.message_handler(commands=["test"])
async def process_test_command(message: types.Message):
    async with aiohttp.ClientSession() as session:
        api_service = ApiService(session)
        posts = await api_service.get_latest_posts()
    await message.answer("Работаю")
