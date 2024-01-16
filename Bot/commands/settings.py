from .callback_data_states import TestCallBackData

from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def command_setting(message: Message):
    setting_markup = InlineKeyboardBuilder()
    setting_markup.button(
        text='Яндекс',
        url='yandex.ru'
    )
    setting_markup.button(
        text='Помощь',
        callback_data=TestCallBackData(text='Привет', user_id=message.from_user.id)
    )
    await message.answer('Настройки', reply_markup=setting_markup.as_markup())


async def call_settings(callback: CallbackQuery, callback_data: TestCallBackData):
    await callback.message.answer(callback_data.text + ', ' + str(callback_data.user_id))
