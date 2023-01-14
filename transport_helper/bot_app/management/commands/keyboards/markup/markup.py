from aiogram.types import KeyboardButton
from aiogram import types

tadd = KeyboardButton("Добавить транспорт")
sadd = KeyboardButton("Добавить остановку")
all = KeyboardButton("Маршруты сохраненого транспорта")
live = KeyboardButton("Сохраненые остановки")
tdell = KeyboardButton("Удалить транспорт")
sdell = KeyboardButton("Удалить остановку")

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(tadd, sadd, all, live, tdell, sdell)