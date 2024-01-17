from select import select
from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy.orm import sessionmaker

from Bot.db import User


class RegisterCheck(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:
        session_maker: sessionmaker = data['session_maker']
        async with session_maker() as session:
            async with session.begin():
                result = await session.execute(statement=select(User).where(User.user_id == event.from_user.id))
                user: User = result.one_or_none()

                if user:
                    pass
                else:
                    user = User(
                        user_id=event.from_user.id,
                        user_name=event.from_user.username
                    )
                await session.merge(user)
                if isinstance(event, Message):
                    await event.answer('Ты успешно зарегистрирован')
                else:
                    await event.message.answer('Ты успешно зарегистрирован')
        return await handler(event, data)
