from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import CommandObject
from config.bot_config import ADMIN
from utils.db_requests import *
import logging

async def handle_deep_link(message: Message, command: CommandObject):
    """Handle deep link for subscriptions"""
    payload = command.args
    if not payload:
        return

    link_type, target_slug = payload.split('_')
    
    user = message.from_user
    add_or_update_user(user.id)
    
    if link_type == 'tag':
        tag_name = subscribe_to_tag(user.id, target_slug)
        if not tag_name:
            await message.answer("Данной категории не существует")
            return
        
        await message.answer(f"Вы подписались на категорию: {tag_name}")
        
    elif link_type == 'author':
        author_name = subscribe_to_author(user.id, target_slug)
        if not author_name:
            await message.answer("Данного автора не существует")
            return

        await message.answer(f"Вы подписались на автора: {author_name}")
        

async def send_author_notification(bot: Bot, user_id: int, author_name: str, title: str, url: str):
    try:
        message = (
            "📢 Новая статья от автора!\n\n"
            f"#{author_name.replace(' ', '_')} опубликовал(a):\n"
            f"<b>{title}</b>\n\n"
            f"👉 <a href='{url}'>Читать статью</a>"
        )
        await bot.send_message(
            chat_id=user_id,
            text=message,
            parse_mode="HTML",
            disable_web_page_preview=False
        )
    except Exception as e:
        logging.error(f"Ошибка отправки уведомления автору {user_id}: {e}")

async def send_tag_notification(bot: Bot, user_id: int, tag_names: list[str], title: str, url: str):
    try:
        hashtags = [f"#{name.replace(' ', '_')}" for name in tag_names]
        tags_text = ", ".join(hashtags)
        message = (
            "📢 Новая статья в ваших категориях!\n\n"
            f"В категориях {tags_text} вышло:\n"
            f"<b>{title}</b>\n\n"
            f"👉 <a href='{url}'>Читать статью</a>"
        )
        await bot.send_message(
            chat_id=user_id,
            text=message,
            parse_mode="HTML",
            disable_web_page_preview=False
        )
    except Exception as e:
        logging.error(f"Ошибка отправки уведомления категории {user_id}: {e}")

async def start_bot_register(bot: Bot):
    await bot.send_message(chat_id=ADMIN, text="Бот перезапущен")


async def stop_bot_register(bot: Bot):
    await bot.send_message(chat_id=ADMIN, text="Бот отключился")
    DB.close()
