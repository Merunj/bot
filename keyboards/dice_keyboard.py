from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('Кинуть 1 шестигранный кубик')
        ],
        [
            KeyboardButton('Кинуть 2 шестигранных кубика')
        ],
        [
            KeyboardButton('Кинуть 20-гранный кубик'), 
        ],
        [
            KeyboardButton('Вернуться назад')
        ],
    ]
)
