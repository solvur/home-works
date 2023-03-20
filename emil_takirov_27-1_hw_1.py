from aiogram.utils import executor
from config import dp
from bot import client, callback, extra, admin, fsmAdminMentor
import logging

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.reg_pin(dp)
fsmAdminMentor.register_handlers_fsm_anketa(dp)
extra.register_handlers_extra(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)