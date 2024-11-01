from kwork import Kwork
from kwork.types import Actor
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()


async def main():
    api = Kwork(login=os.getenv('login'), password=os.getenv('password'))
    me: Actor = await api.get_me()
    # Получение своего профиля
    print(me)
    await api.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())