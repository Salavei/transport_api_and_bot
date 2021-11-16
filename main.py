from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from parser import parser_time_wait
import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook
from settings import (BOT_TOKEN, HEROKU_APP_NAME,
                          WEBHOOK_URL, WEBHOOK_PATH,
                          WEBAPP_HOST, WEBAPP_PORT)

# token = '2103715376:AAFeYeMDV_73TrtT3gAPID_rcGp0LsXau80'


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = """Это бот для просмотра транспорта
    введи по порядку город, транспорт, номер транспорта, остановку
    города: minsk, brest, vitebsk, grodno, gomel, mogilev
    транспорт: autobus, trolleybus, tram, metro"""
    send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(send_message.to_python())


@dp.message_handler(commands=['home'])
async def get_message(message: types.Message):
    trans_data = parser_time_wait('minsk', 'autobus', '24', 'Воронянского%20-%20ДС%20Зелёный%20Луг-6/Жуковского')
    chat_id = message.chat.id
    text = f'От дома --- прошлый был в {trans_data[0]}, следующий в {trans_data[1]}'
    send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(send_message.to_python())


@dp.message_handler(commands=['work'])
async def get_message(message: types.Message):
    trans_data = parser_time_wait('minsk', 'autobus', '24', 'ДС%20Зелёный%20Луг-6%20-%20Воронянского/Романовская%20Слобода')
    chat_id = message.chat.id
    text = f'От работы --- прошлый был в {trans_data[0]}, следующий в {trans_data[1]}'
    send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(send_message.to_python())


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     up_msg = msg.text
#     msg = up_msg.split()
#     print(msg)
    # await bot.send_message(msg.from_user.id, msg.text)
    # принимать значение о транспорте и т/д


def main():
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )