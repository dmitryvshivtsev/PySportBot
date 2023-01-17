from aiogram import types
from aiogram.filters import CommandObject
from bot.commands.parsing import send_date_of_match


async def get_sport():
    pass


async def get_teams():
    pass


async def get_date(message: types.Message, command: CommandObject) -> None:
    try:
        await message.answer(send_date_of_match(command.args))
    except:
        await message.answer('Для этой команды не можем найти матчи :(')