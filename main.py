from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from parser import parser_time_wait, parser_station, parser_all_station

token = '2103715376:AAFeYeMDV_73TrtT3gAPID_rcGp0LsXau80'

bot = Bot(token)
dp = Dispatcher(bot)


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


@dp.message_handler(commands=['station'])
async def parser_station(message: types.Message):
    trans_data = parser_station('minsk', 'autobus', '24')
    chat_id = message.chat.id
    text = f'Направления 24 автобуса \n {trans_data}'
    send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(send_message.to_python())

@dp.message_handler(commands=['allstation'])
async def parser_station(message: types.Message):
    trans_data = parser_all_station('minsk', 'autobus', '24')
    chat_id = message.chat.id
    text = f'Все остановки 24 автобуса \n {trans_data}'
    send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(send_message.to_python())

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     up_msg = msg.text
#     msg = up_msg.split()
#     print(msg)
    # await bot.send_message(msg.from_user.id, msg.text)
    # принимать значение о транспорте и т/д


if __name__ == '__main__':
    executor.start_polling(dp)
