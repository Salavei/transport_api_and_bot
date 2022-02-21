from aiogram import Bot, Dispatcher, executor
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from ugc.management.commands.utils.api.aidb import SQLestate
from pathlib import Path
import environ
from tga.settings import TOKEN, DATABASES_LOCATION

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(env_file=str(BASE_DIR) + '/.env')

adb = SQLestate(DATABASES_LOCATION)
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

if __name__ == '__main__':
    from handlers.users.app import dp

    print('Start bot...')
    executor.start_polling(dp, skip_updates=True)
