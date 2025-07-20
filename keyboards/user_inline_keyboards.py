from aiogram.utils.keyboard import *
from utils.db_requests import *


# def user_keyboard_builder_feedback():
#     builder = InlineKeyboardBuilder()
#     builder.button(text="Связаться с администратором", url=f"tg://user?id={MANAGER}")
#     builder.button(text="Назад ⬅️", callback_data=f"none")

#     builder.adjust(1)
#     return builder.as_markup()


# def user_keyboard_builder_speakers():
#     builder = InlineKeyboardBuilder()
#     event_speakers = get_event_speakers(get_current_event()["id"])
#     for speaker in event_speakers or []:
#         builder.button(
#             text=f"{speaker['name']}",
#             callback_data=f"ask_speaker?id={speaker['id']}",
#         )
#     builder.button(text="Назад ⬅️", callback_data=f"none")

#     builder.adjust(2)
#     return builder.as_markup(one_time_keyboard=True)


# def user_keyboard_builder_variants(quiz_id):
#     builder = InlineKeyboardBuilder()

#     quiz_variants = get_quiz_variants(quiz_id)
#     for i in range(0, len(quiz_variants or [])):
#         builder.button(
#             text=f"{i+1}",
#             callback_data=f"survey_answer?id={quiz_variants[i]['id']}",
#         )

#     return builder.as_markup()


# user_keyboard_survey_start = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Поехали 🚀", callback_data="survey_start")],
#         [InlineKeyboardButton(text="Назад ⬅️", callback_data="none")],
#     ]
# )

# user_keyboard_survey_end = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Завершить 🏁", callback_data="survey_end")],
#     ]
# )


# user_keyboard_confirm = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Отправить ✅", callback_data="send_question")],
#         [InlineKeyboardButton(text="Отмена ❌", callback_data="none")],
#     ]
# )

# user_keyboard_cancel = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Отмена ❌", callback_data="none")],
#     ]
# )
