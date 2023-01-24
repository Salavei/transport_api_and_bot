from aiogram.types import KeyboardButton
from aiogram import types

tadd = KeyboardButton("Add transport")
sadd = KeyboardButton("Add a stop")
all = KeyboardButton("Saved transport routes")
live = KeyboardButton("Saved stops")
tdell = KeyboardButton("Delete transport")
sdell = KeyboardButton("Delete stop")

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(tadd, sadd, all, live, tdell, sdell)