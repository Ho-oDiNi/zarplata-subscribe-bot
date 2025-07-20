from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from keyboards.user_inline_keyboards import *
from utils.registers import *

router = Router()

@router.message(Command("start", "restart", "Start", "Restart"))
async def user_handler_menu(message: Message, command: CommandObject):
    if command.args:
        await handle_deep_link(message, command)
    else:
        await message.answer("Привет! Подпишись на категорию или автора, чтобы получать уведомления!")



# @router.message(F.text.lower().in_({"пройти опрос 📊", "пройти опрос"}))
# async def user_handler_quiz(message: Message, bot: Bot):
#     await bot.delete_message(message.from_user.id, get_msg_id(message.from_user.id))
#     await bot.send_chat_action(message.from_user.id, action="typing")

#     if get_by_tg_id(message.from_user.id)["is_passed"]:
#         msg = await bot.send_photo_if_exist(
#             chat_id=message.from_user.id,
#             caption=FSInputFile("images/already-gone.webp"),
#             text="Опрос уже пройден",
#             reply_markup=user_keyboard_main,
#         )
#         set_msg_id(message.from_user.id, msg.message_id)
#         await bot.delete_message(message.from_user.id, message.message_id)
#         return

#     msg = await bot.send_photo_if_exist(
#         chat_id=message.from_user.id,
#         caption=FSInputFile("images/are-u-ready.webp"),
#         text=f"Готовы начать?",
#         reply_markup=user_keyboard_survey_start,
#     )

#     await bot.delete_message(message.from_user.id, message.message_id)
#     set_msg_id(message.from_user.id, msg.message_id)
