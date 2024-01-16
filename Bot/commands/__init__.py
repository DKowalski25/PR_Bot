__all__ = ['register_user_command', 'bot_commands']

from aiogram import Router, F
from aiogram.filters import Command, CommandStart

from Bot.commands.start import command_start
from Bot.commands.help import command_help, help_func, call_help_func
from Bot.commands.settings import command_setting, call_settings

from .callback_data_states import TestCallBackData


def register_user_command(router: Router) -> None:
    router.message.register(command_start, CommandStart())
    router.message.register(command_help, Command(commands=['help']))
    router.message.register(help_func, F.text == 'Помощь')
    router.message.register(command_setting, Command(commands=['settings']))

    router.callback_query.register(call_help_func, F.data == 'help')
    router.callback_query.register(call_settings,  TestCallBackData.filter())
