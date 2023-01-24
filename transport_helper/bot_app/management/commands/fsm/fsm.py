from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import dp, adb
from parser import parser_station_n, parser_all_station


class FSMstationadd(StatesGroup):
    type_transport = State()
    number_transport = State()
    name_station = State()

async def add_station_start(message: types.Message):
    await FSMstationadd.type_transport.set()
    await message.answer('Enter the name of the transport (Bus, Tram, Trolleybus):')


@dp.message_handler(state=FSMstationadd.type_transport)
async def write_type_transport_add_station(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type_transport'] = message.text
    await FSMstationadd.next()
    await message.answer('Enter the vehicle number:')


@dp.message_handler(state=FSMstationadd.number_transport)
async def write_number_transport_add_station(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_transport'] = message.text
        await FSMstationadd.next()
        await message.answer('Enter the name of the stop:')


@dp.message_handler(state=FSMstationadd.name_station)
async def write_name_station_add_station(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_station'] = message.text
        await FSMstationadd.next()
        if 'Incorrect' not in parser_station_n(data['type_transport'], data['number_transport'],
                                       data['name_station'][0].upper() + data['name_station'][1:].lower()):
            adb.add_stats(transport_type=data['type_transport'], transport_number=data['number_transport']
                          , station=f"{data['name_station'][0].upper() + data['name_station'][1:].lower()}",
                          external_id=adb.give_user_id(message.from_user.id)[0])
            await message.answer(
                text=f"✨ The route from the stop 🚏: {data['name_station'][0].upper()}{data['name_station'][1:].lower()} added ✅")
        else:
            await message.answer(text=f"❌ Wrong transport name! ❌")
        await state.finish()


class FSMadd_transport(StatesGroup):
    type_transport = State()
    number_transport = State()


async def add_transport_start(message: types.Message):
    await FSMadd_transport.type_transport.set()
    await message.answer('Enter the name of the transport (Bus, Tram, Trolleybus):')


@dp.message_handler(state=FSMadd_transport.type_transport)
async def write_type_transport(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type_transport'] = message.text
    await FSMadd_transport.next()
    await message.answer('Enter the vehicle number:')


@dp.message_handler(state=FSMadd_transport.number_transport)
async def write_number_transport(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_transport'] = message.text
        await FSMadd_transport.next()
        if 'Incorrect' not in parser_all_station(data['type_transport'], data['number_transport']):
            adb.add_tran(transport_type=data['type_transport'], transport_number=data['number_transport'],
                         external_id=adb.give_user_id(message.from_user.id)[0])
            await message.answer(text=f"✨ Transport 🚍: {data['type_transport']} {data['number_transport']} added ✅")
        else:
            await message.answer(text=f"❌ Wrong transport name! ❌")
        await state.finish()
