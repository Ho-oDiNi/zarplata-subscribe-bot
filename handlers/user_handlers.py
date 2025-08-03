from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from utils.registers import *

router = Router()

@router.message(Command("start", "restart", "Start", "Restart"))
async def user_handler_menu(message: Message, command: CommandObject):
    if command.args:
        await handle_deep_link(message, command)
    else:
        await message.answer("Привет! Подпишись на категорию или автора, чтобы получать уведомления!")
