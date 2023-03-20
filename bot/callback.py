from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp, Dispatcher


# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_2)
    question = "Как кастануть Торнадо?"
    answer = [
        "QQW",
        "WWQ",
        "EEW",
        "WWE",
        "QQE",
        "EEQ",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "5+5?"
    answer = [
        "1",
        "2",
        "10",
        "15",
        "14",
        "26",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")


