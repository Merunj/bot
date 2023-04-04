from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('Вход')
        ]
    ]
)

first_state_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('2'),
            KeyboardButton('Выход')
        ]
    ]
)

second_state_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('3')
        ]
    ]
)

third_state_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('1'),
            KeyboardButton('4')            
        ]
    ]
)

fourth_state_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('1')
        ]
    ]
)