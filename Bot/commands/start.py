from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, KeyboardButtonPollType


async def command_start(message: Message) -> None:
    """The function process the 'start' command."""
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.button(
        text='Помощь'
    )
    menu_builder.add(
        KeyboardButton(text='Отправить контакт', request_contact=True),
    )
    menu_builder.row(
        KeyboardButton(text='Отправить голосование', request_poll=KeyboardButtonPollType(type=None))
    )
    await message.answer(
        'Меню',
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
    )
