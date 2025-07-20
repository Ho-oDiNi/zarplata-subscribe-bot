from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import CommandObject
from config.bot_config import ADMIN
from utils.db_requests import *

async def handle_deep_link(message: Message, command: CommandObject):
    """Handle deep link for subscriptions"""
    payload = command.args
    if not payload:
        return

    link_type, target_slug = payload.split('_')
    
    user = message.from_user
    add_or_update_user(user.id)
    
    if link_type == 'category':
        category_name = subscribe_to_category(user.id, target_slug)
        if not category_name:
            await message.answer("Данной категории не существует")
            return
        
        await message.answer(f"Вы подписались на категорию: {category_name}")
        
    elif link_type == 'author':
        author_name = subscribe_to_author(user.id, target_slug)
        if not author_name:
            await message.answer("Данного автора не существует")
            return

        await message.answer(f"Вы подписались на автора: {author_name}")
        

async def start_bot_register(bot: Bot):
    await bot.send_message(chat_id=ADMIN, text="Бот перезапущен")


async def stop_bot_register(bot: Bot):
    await bot.send_message(chat_id=ADMIN, text="Бот отключился")
    DB.close()
