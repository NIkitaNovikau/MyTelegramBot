from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_start_vzv() -> InlineKeyboardMarkup:
    vzv = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('1 взвод', callback_data='get_all_kursant')],
        [InlineKeyboardButton('2 взвод', callback_data='get_all_kursant')],
        [InlineKeyboardButton('3 взвод', callback_data='get_all_kursant')]
    ])
    return vzv


def get_start_obl() -> InlineKeyboardMarkup:
    obl = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Минск', callback_data='get_all_kursant')],
        [InlineKeyboardButton('Минская область', callback_data='get_all_kursant')],
        [InlineKeyboardButton('Брестская область', callback_data='get_all_kursant')],
        [InlineKeyboardButton('Витебская область', callback_data='get_all_kursant')],
        [InlineKeyboardButton('Могилевская область', callback_data='get_all_kursant')],
        [InlineKeyboardButton('Гомельская область', callback_data='get_all_kursant')],
        [InlineKeyboardButton('Гродненская область', callback_data='get_all_kursant')]
    ])
    return obl


def get_find() -> ReplyKeyboardMarkup:
    fnd = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
        [
            KeyboardButton(text='Поиск по области.'),
        ],
        [
            KeyboardButton(text='Получение информации по взводам.')
        ],
        [
            KeyboardButton(text='Поиск по фамилии.')
        ]
    ])
    return fnd


def get_create_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/createProfile'))
    return kb


def get_cancel_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/cancelProfile'))
    return kb