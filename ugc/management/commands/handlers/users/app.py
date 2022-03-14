from aiogram.dispatcher.filters.builtin import CommandStart
from ugc.management.commands.main import dp, adb
from ugc.management.commands.keyboards.markup.markup import keyboard
from ugc.management.commands.utils.funk_async import *
from ugc.management.commands.parser import parser_all_station, parser_station_n


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not adb.check_subscriber(message.from_user.id):
        adb.add_subscriber(message.from_user.id)
        await message.answer(f'Привет! Давай я помогу тебе поскорее добраться до точки назначения🔜 /help',
                             reply_markup=keyboard)
    await message.answer(f'Привет! Давай я помогу тебе поскорее добраться до точки назначения🔜 /help',
                         reply_markup=keyboard)


async def error(message: types.Message):
    if len(message.text.split(' ')) == 2 and '❌' not in parser_all_station(message.text.split(' ')[0], message.text.split(' ')[1]):
        await message.answer(
            text=f'{message.text} ✨ Все остановки🚏')
        await message.answer(
            text=f"⬅️{parser_all_station(message.text.split(' ')[0], message.text.split(' ')[1])[0]}\n\n➡️{parser_all_station(message.text.split(' ')[0], message.text.split(' ')[1])[1]}")
    elif len(message.text.split(' ')) > 2  and '❌' not in parser_station_n(message.text.split(' ')[0], message.text.split(' ')[1], message.text.split(' ')[2]):

        await message.answer(
            text=f"✨ Транспорт: {message.text.split(' ')[0]}, {message.text.split(' ')[1]}\nОстановка 🚏 {message.text.split(' ')[2]}:")
        await message.answer(
            text=f"{parser_station_n(message.text.split(' ')[0], message.text.split(' ')[1], message.text.split(' ')[2])[0]}\n{parser_station_n(message.text.split(' ')[0], message.text.split(' ')[1], message.text.split(' ')[2])[1]}")
    else:
        await message.answer(text='⚠️Проверьте написание названия транспорта!!')

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
        'Добавить транспорт': add_new_transport,
        'Добавить остановку': add_new_station,
        'Маршруты сохраненого транспорта': show_save_transport,
        'Сохраненые остановки': show_save_station,
        'Удалить транспорт': dell_save_transport,
        'Удалить остановку': dell_save_station,
    }
    await data.get(message.text, error)(message)
