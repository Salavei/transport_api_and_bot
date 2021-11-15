from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from parser import parser_data

token = '2114179429:AAGxSBcMwbFzxmPtYTtyIzmykrnkSCYhbqk'

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['home'])
async def get_message(message: types.Message):
    trans_data = parser_data('minsk','autobus','24','Воронянского%20-%20ДС%20Зелёный%20Луг-6/Жуковского')
    chat_id = message.chat.id
    text = f'От дома --- прошлый был в {trans_data[0]}, следующий в {trans_data[1]}'
    send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(send_message.to_python())


@dp.message_handler(commands=['work'])
async def get_message(message: types.Message):
    trans_data = parser_data('minsk', 'autobus', '24', 'ДС%20Зелёный%20Луг-6%20-%20Воронянского/Романовская%20Слобода')
    chat_id = message.chat.id
    text = f'От работы --- прошлый был в {trans_data[0]}, следующий в {trans_data[1]}'
    send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(send_message.to_python())

if __name__ == '__main__':
    executor.start_polling(dp)
