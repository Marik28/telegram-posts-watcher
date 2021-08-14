import asyncio

from aiogram.utils import executor

from .bot import dp, check_posts_and_send_messages
from .database import engine
from .tables import Base

Base.metadata.create_all(engine)
loop = asyncio.get_event_loop()
loop.create_task(check_posts_and_send_messages(10))

executor.start_polling(dp)
