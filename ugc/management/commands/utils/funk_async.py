from aiogram import types
from ugc.management.commands.main import adb
from ugc.management.commands.fsm.fsm import add_transport_start, add_station_start
from ugc.management.commands.parser import *


async def show_save_transport(message: types.Message):
    if not adb.count_transp(*adb.give_user_id(message.from_user.id)):
        await message.answer(text='❌ Вы еще не добавили ни одного транспорта ❌')
    elif adb.count_transp(*adb.give_user_id(message.from_user.id)) < 2:
        await message.answer(
            text=f'{adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[0]} ✨ Все остановки🚏')
        await message.answer(
            text=f'⬅️{parser_all_station(*adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[0])[0]}\n\n➡️{parser_all_station(*adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[0])[1]}')
    else:
        await message.answer(
            text=f'{adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[0]} ✨ Все остановки🚏')
        await message.answer(
            text=f'⬅️{parser_all_station(*adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[0])[0]}\n\n➡️{parser_all_station(*adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[0])[1]}')
        await message.answer(
            text=f'{adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[1]} ✨ Все остановки🚏')
        await message.answer(
            text=f'⬅️{parser_all_station(*adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[1])[0]}\n\n➡️{parser_all_station(*adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[1])[1]}')


async def show_save_station(message: types.Message):
    if not adb.count_station(*adb.give_user_id(message.from_user.id)):
        await message.answer(text='❌ Вы еще не добавили ни остановок ❌')
    elif adb.count_station(*adb.give_user_id(message.from_user.id)) < 2:
        await message.answer(
            text=f'✨ Транспорт {adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[0][1]}\nОстановка 🚏 {adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[0][2]}:')
        await message.answer(
            text=f"{parser_station_n(*adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[0])[1]}\n{parser_station_n(*adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[0])[0]}")
    else:
        await message.answer(
            text=f'✨ Транспорт {adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[0][1]}\nОстановка 🚏 {adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[0][2]}:')
        await message.answer(
            text=f"{parser_station_n(*adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[0])[1]}\n{parser_station_n(*adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[0])[0]}")

        await message.answer(
            text=f'✨  Транспорт {adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[1][1]}\nОстановка 🚏 {adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[1][2]}:')
        await message.answer(
            text=f"{parser_station_n(*adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[1])[1]}\n{parser_station_n(*adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[1])[0]}")


async def add_new_transport(message: types.Message):
    """ Сделать проверку на текст """
    if adb.count_transp(*adb.give_user_id(message.from_user.id)) < 2:
        await add_transport_start(message)
    else:
        await message.answer(text='❌ Нельзя добавить больше 2-ух транспорта❌')


async def add_new_station(message: types.Message):
    """ Сделать проверку на текст """
    if adb.count_station(*adb.give_user_id(message.from_user.id)) < 2:
        await add_station_start(message)
    else:
        await message.answer(text='❌ Нельзя добавить больше 2-ух остановок ❌')


async def dell_save_transport(message: types.Message):
    """ Сделать удаление последнего """
    if not adb.show_all_my_transport(*adb.give_user_id(message.from_user.id)):
        await message.answer(text='❌ У вас еще нет транспорта чтобы его удалить ❌')
    else:
        adb.dell_my_transport(*adb.give_user_id(message.from_user.id))
        await message.answer(text='⚠️Удалили транспорт')


async def dell_save_station(message: types.Message):
    """ Сделать удаление последнего """
    if not adb.show_all_my_station(*adb.give_user_id(message.from_user.id)):
        await message.answer(text='❌ У вас еще нет остановок чтобы их удалить ❌')
    else:
        adb.dell_my_station(*adb.give_user_id(message.from_user.id))
        await message.answer(text='⚠️Удалили остановку')


async def about_help(message: types.Message):
    await message.answer(text=
                         f'\nЕсли введешь:'
                         f'\n➡️ вид интересующего тебя транспорта и его номер - откроется полный список остановок на его маршруте'
                         f'\n➡️ Пример: Автобус 100'
                         f'\n➡️ вид транспорта, его номер и название остановки - увидишь время отправления транспорта'
                         f'\n➡️ ☝️ВАЖНО: если остановка начинается что-то вроде Площадь / Станция и т.д, ❗️писать нужно само название - Немига, Якуба, Победы❗️️'
                         f'\n➡️ Пример: Автобус 100 Козлова'
                         f'\n➡️ /tadd - добавишь далее введённый транспорт в избранные (не более 2-х)'
                         f'\n➡️ /sadd - добавишь далее введённую остановку в избранные (не более 2-х)'
                         f'\n➡️ /all - получишь все остановки избранного транспорта'
                         f'\n➡️ /live - узнаешь время отправления избранного транспорта с избранной остановки'
                         f'\n➡️ /tdell - удалишь избранный транспорт'
                         f'\n➡️ /sdell - удалишь избранную остановку'
                         f'\nУдачи и в путь!😊')
