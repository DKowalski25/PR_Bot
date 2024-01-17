import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from sqlalchemy.engine import URL

from commands import register_user_command
from commands.bot_commands import bot_commands

from db import BaseModel, create_engine, get_session_maker, proceed_schemas, User


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(token=os.getenv('token'))

    await bot.set_my_commands(commands=commands_for_bot)

    register_user_command(dp)

    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=os.getenv('db_user'),
        host='localhost',
        password=os.getenv('db_pass'),
        database=os.getenv('db_name'),
        port=os.getenv('db_port')
    )

    async_engin = create_engine(postgres_url)
    session_maker = get_session_maker(async_engin)
    await proceed_schemas(async_engin, BaseModel.metadata)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot Stopped')
