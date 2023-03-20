from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
ADMINS = (1019059760, )

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)