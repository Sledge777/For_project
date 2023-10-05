from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, inline_keyboard_markup, inline_keyboard_button

user_main_kb= [
    [KeyboardButton(text='❓узнать о боте'),

    ],
    [KeyboardButton(text='💩ара какиш'),
     
     ]
    
]

user_main = ReplyKeyboardMarkup(keyboard=user_main_kb, resize_keyboard=True, input_field_placeholder='')