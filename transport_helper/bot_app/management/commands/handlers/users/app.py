from aiogram.dispatcher.filters.builtin import CommandStart
from main import dp
from keyboards.markup.markup import keyboard
from utils.funk_async import *
from parser import parser_all_station, parser_station_n


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if adb.check_subscriber(message.from_user.id):
        await message.answer(f'Hi! Let me help you get to your destination quickly🔜 /help',
                         reply_markup=keyboard)
    else:
        adb.add_subscriber(message.from_user.id)
        await message.answer(f'Hi! Let me help you get to your destination quickly🔜 /help',
                         reply_markup=keyboard)


async def error(message: types.Message):
    if len(message.text.split(' ')) == 2 and 'Incorrect' not in parser_all_station(message.text.split(' ')[0], message.text.split(' ')[1]):
        await message.answer(
            text=f'{message.text} ✨ All stops🚏')
        await message.answer(
            text=f"⬅️{parser_all_station(message.text.split(' ')[0], message.text.split(' ')[1])[0]}\n"
                 f"\n➡️{parser_all_station(message.text.split(' ')[0], message.text.split(' ')[1])[1]}")
    elif len(message.text.split(' ')) > 2 and 'Incorrect' not in parser_station_n(message.text.split(' ')[0],
                                                                          message.text.split(' ')[1], message.text.split(' ')[2]):

        await message.answer(
            text=f"✨ Transport: {message.text.split(' ')[0]}, {message.text.split(' ')[1]}\nStop 🚏 {message.text.split(' ')[2]}:")
        station = parser_station_n(message.text.split(' ')[0], message.text.split(' ')[1], message.text.split(' ')[2])
        await message.answer(
            text=f"{station[0][0]} :\n{station[0][1]} - {station[0][2]}\n"
                 f"{station[1][0]} :\n{station[1][1]} - {station[1][2]}"
        )

    else:
        await message.answer(text='⚠️Check the spelling of the name of the transport!!!')


@dp.message_handler(content_types=['text'])
async def command_start_text(message: types.Message):
    data = {
        '/help': about_help,
        '/tadd': add_new_transport,
        '/sadd': add_new_station,
        '/all': show_save_transport,
        '/live': show_save_station,
        '/tdell': dell_save_transport,
        '/sdell': dell_save_station,
        'Add transport': add_new_transport,
        'Add a stop': add_new_station,
        'Saved transport routes': show_save_transport,
        'Saved stops': show_save_station,
        'Delete transport': dell_save_transport,
        'Delete stop': dell_save_station,
    }
    await data.get(message.text, error)(message)
