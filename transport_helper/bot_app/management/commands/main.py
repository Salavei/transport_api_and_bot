from aiogram import Bot, Dispatcher, executor
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.api.aidb import SQLestate
import os


TOKEN = os.environ.get('TOKEN')

adb = SQLestate()
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

if __name__ == '__main__':
    from handlers.users.app import dp
    print('Start bot...')
    executor.start_polling(dp, skip_updates=True)
