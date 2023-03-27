import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.bot_db import sql_command_all_id
from apscheduler.triggers.date import DateTrigger
from config import bot, ADMINS


async def message(bot: Bot):
    user_ids = await sql_command_all_id()
    for user_id in user_ids:
        await bot.send_message(user_id[0], "С днём рождения!")

async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')


    scheduler.add_job(
        message,
        trigger=DateTrigger(
            run_date=datetime.datetime(year=2023, month=10, day=30, hour=8, minute=30)
        ),
        kwargs = {"bot": bot},
        )

    scheduler.start()