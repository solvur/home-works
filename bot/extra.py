from aiogram import types, Dispatcher
from config import bot
from random import random


dice = ['⚽', '🏀', '🎰', '🎯', '🎳', '🎲']


async def game(message: types.Message):
    if message.text.lower() == 'game':
        await bot.send_message(message.message_id)


async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)
    def register_handlers_extra(dp: Dispatcher):
        dp.register_message_handler(content_types=['text'])

    if message.text.startswith('!pin'):
        await message.pin()


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(game)
    dp.register_message_handler(echo)
