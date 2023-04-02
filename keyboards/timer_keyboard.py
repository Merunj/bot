from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('30 секунд'),
            KeyboardButton('1 минута'),
            KeyboardButton('5 минут')
        ],
        [
            KeyboardButton('Вернуться назад'), 
        ],
    ]
)