from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, inline_keyboard_markup, inline_keyboard_button
from aiogram.types.web_app_info import WebAppInfo

user_main_kb= [
    [KeyboardButton(text='Управление ботом', web_app=WebAppInfo(url='https://master--animated-rugelach-7c0140.netlify.app/telegram')), 

    ],
    
]

user_main = ReplyKeyboardMarkup(keyboard=user_main_kb, resize_keyboard=True, input_field_placeholder='')