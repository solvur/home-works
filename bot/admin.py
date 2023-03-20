from aiogram import types, Dispatcher
from config import bot


async def pin(message: types.Message):
    if message.chat.type != 'private':
        await bot.pin_chat_message(message.chat.id, message.message_id)
    else:
        await message.answer('Чё-то попутал')


def reg_pin(db: Dispatcher):
    db.register_message_handler(pin, commands=['pin'], commands_prefix=['!'])
