from aiogram import types
from main import adb
from fsm.fsm import add_transport_start, add_station_start
from parser import *


async def show_save_transport(message: types.Message):
    if not adb.count_transp(*adb.give_user_id(message.from_user.id)):
        await message.answer(text="❌ You haven't added any vehicles yet ❌")
    for step in range(adb.count_transp(*adb.give_user_id(message.from_user.id))):
        await message.answer(
            text=f'{adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[step][0]} '
                 f'{adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[step][1]} ✨ All stops🚏')
        await message.answer(
            text=f'⬅️{parser_all_station(*adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[step])[0]}\n'
                 f'\n➡️{parser_all_station(*adb.show_all_my_transport(*adb.give_user_id(message.from_user.id))[step])[1]}')


async def show_save_station(message: types.Message):
    if not adb.count_station(*adb.give_user_id(message.from_user.id)):
        await message.answer(text='❌ You have not yet added any stops ❌')
    for step in range(adb.count_station(*adb.give_user_id(message.from_user.id))):
        await message.answer(
            text=f'✨ Transport {adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[step][1]}\n'
                 f'Stop 🚏 {adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[step][2]}:')
        station = parser_station_n(*adb.show_all_my_station(*adb.give_user_id(message.from_user.id))[0])
        await message.answer(
            text=f"{station[0][0]} :\n{station[0][1]} - {station[0][2]}\n"
                 f"{station[1][0]} :\n{station[1][1]} - {station[1][2]}"
        )


async def add_new_transport(message: types.Message):
    """ Do a text check """
    if adb.count_transp(*adb.give_user_id(message.from_user.id)) < 2:
        await add_transport_start(message)
    else:
        await message.answer(text='❌ You cannot add more than 2 vehicles ❌')


async def add_new_station(message: types.Message):
    """ Do a text check """
    if adb.count_station(*adb.give_user_id(message.from_user.id)) < 2:
        await add_station_start(message)
    else:
        await message.answer(text='❌ You cannot add more than 2 stops ❌')


async def dell_save_transport(message: types.Message):
    """ Do a text check """
    if not adb.show_all_my_transport(*adb.give_user_id(message.from_user.id)):
        await message.answer(text="❌ You don't have the transport to remove it yet ❌")
    else:
        info_delete_transport = adb.dell_my_transport(*adb.give_user_id(message.from_user.id))[0]
        await message.answer(
            text=f'⚠️Removed the transport {info_delete_transport[0]} {info_delete_transport[1]}')


async def dell_save_station(message: types.Message):
    """ Do a text check """
    if not adb.show_all_my_station(*adb.give_user_id(message.from_user.id)):
        await message.answer(text="❌ You don't have the stops to delete them yet ❌")
    else:
        info_delete_station = adb.dell_my_station(*adb.give_user_id(message.from_user.id))[0]
        await message.answer(
            text=f'⚠️The stop was deleted {info_delete_station[0]} {info_delete_station[1]} {info_delete_station[2]}')


async def about_help(message: types.Message):
    await message.answer(text=
                         f'\nIf you enter:'
                         f'\n➡️ the type and number of the vehicle you are interested in will open a complete list of stops on its route'
                         f'\n➡️ Example: Bus 100'
                         f'\n➡️ type of transport, its number and name of stop - you will see the time of departure'
                         f'\n➡️ ☝️IMPORTANT: if the stop starts something like Square / Station etc., ❗write you need the name itself - Немига, Якуба, Победы❗️️'
                         f'\n➡️ Example: Bus 100 Козлова'
                         f'\n➡️ /tadd - add further entered transport to favorites (not more than 2)'
                         f'\n➡️ /sadd - add further entered stop to favorites (not more than 2)'
                         f'\n➡️ /all - get all the stops of the favorite transport'
                         f'\n➡️ /live - you will get the time of departure of the favorite stop'
                         f'\n➡️ /tdell - delete the chosen transport'
                         f'\n➡️ /sdell - delete favorite stop'
                         f'\Good luck and hit the road!'
                         )
