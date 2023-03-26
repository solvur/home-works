from aiogram.utils import executor
from config import dp, bot, ADMINS
from bot import client, callback, extra, admin, fsmAdminMentor
import logging
from database.bot_db import sql_create

async def on_startup(_):
    await bot.send_message(ADMINS[0], 'Привет')
    sql_create()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)