from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile
from keyboards.user_inline_keyboards import *


router = Router()


# @router.callback_query(F.data == "survey_start")
# async def start_survey(callback: CallbackQuery, state: FSMContext, bot: Bot):
#     await bot.delete_message(callback.from_user.id, get_msg_id(callback.from_user.id))

#     await state.set_state(Survey.quizId)
#     quiz = get_next_quiz()

#     await state.update_data(quizId=quiz["id"])

#     msg = await bot.send_photo_if_exist(
#         chat_id=callback.from_user.id,
#         caption=quiz["img"],
#         text=f"{parse_quiz_content(quiz)}",
#         reply_markup=user_keyboard_builder_variants(quiz["id"]),
#     )

#     set_msg_id(callback.from_user.id, msg.message_id)




@router.callback_query(F.data == "none")
async def cancel(callback: CallbackQuery, state: FSMContext, bot: Bot):

    msg = await bot.send_photo_if_exist(
        chat_id=callback.from_user.id,
        caption=FSInputFile("images/action-cancell.webp"),
        text=f"Действие отменено",
        reply_markup=user_keyboard_main,
    )

