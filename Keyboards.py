from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text="20’DC"), KeyboardButton("40’DC"), KeyboardButton("40’HC"), KeyboardButton("Перезвоните мне"))

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb2.add(KeyboardButton('Главное меню'))
