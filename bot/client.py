from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot

# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Приветствую!")


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("quiz-для вопроса\n"
                         "meme-для мемчика"
                         "")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)
    question = "2+2?"
    answer = [
        "16",
        "Да",
        "4",
        "7423894732",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Не правильно",
        open_period=10,
        reply_markup=markup
    )


# @dp.message_handler(commands=['meme'])
async def send_ph(message: types.Message):
    idphoto123 = 'AgACAgIAAxkBAANwZA1l1i-lMYtxzRgEW4P9j_ZLv8kAAnvEMRuAH3FIrA1eX8oHqawBAAMCAAN4AAMvBA'
    await message.reply_photo(idphoto123)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])