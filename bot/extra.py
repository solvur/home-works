from aiogram import types, Dispatcher
from config import bot
from random import random
from sender import video, audio


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


async def send_video(message: types.Message):
    if "youtube.com" in message.text:
        await message.answer("Загружаю видео")
        downloader_video = open(f"../{video(message.text)}", "rb")
        await message.answer_video(downloader_video)
        await message.answer("Загрузил!")


async def send_audio(message: types.Message):
    if "youtube.com" in message.text:
        await message.answer("Загружаю имбовый трек")
        downloader_audio = open(f"../{audio(message.text)}", "rb")
        await message.answer_video(downloader_audio)
        await message.answer("Загрузил!")


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(game)
    dp.register_message_handler(echo)
