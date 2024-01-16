from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandObject

from Bot.commands.bot_commands import bot_commands


async def command_help(message: Message, command: CommandObject):
    """The function process the 'help' command."""
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(
                    f'{cmd[0]} - {cmd[1]}\n\n{cmd[2]}'
                )
        else:
            return await message.answer('Команда не найдена')
    return help_func(message)


async def help_func(message: Message):
    return await message.answer(
        'Помощь и справка о боте\n'
        'Для того чтобы получить информацию о команде используйте /help <команда>\n'
    )


async def call_help_func(callback: CallbackQuery):
    await callback.message.edit_text(
        'Помощь и справка о боте\n'
        'Для того чтобы получить информацию о команде используйте /help <команда>\n',
        reply_markup=callback.message.reply_markup
    )
