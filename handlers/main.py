from loader import dp
from keyboards.both_keyboards import *
from states.states import Room_State

@dp.message_handler(commands=['start'])
async def start_command(msg):
    await msg.answer('Привет! Ты на входе в музей.', reply_markup=start_keyboard)
    await Room_State.start_museum.set()

@dp.message_handler(state=Room_State.start_museum)
async def museum(msg):
    await msg.answer('Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!', reply_markup=first_state_keyboard)
    await Room_State.room_1.set()

@dp.message_handler(state=Room_State.room_1)
async def first_state_func(msg):
    if msg.text == '2':
        await msg.answer('В данном зале представлены картины', reply_markup=second_state_keyboard)
        await Room_State.room_2.set()
    elif msg.text == 'Выход':
        await msg.answer('Всего доброго, не забудьте забрать верхнюю одежду в гардеробе!', reply_markup=start_keyboard)
        await Room_State.start_museum.set()
    else:
        await msg.answer('Нет такого варианта')

@dp.message_handler(state=Room_State.room_2)
async def second_state_func(msg):
    if msg.text == '3':
        await msg.answer('В данном зале представлены яйца Фаберже', reply_markup=third_state_keyboard)
        await Room_State.room_3.set()
    else:
        await msg.answer('Нет такого варианта')

@dp.message_handler(state=Room_State.room_3)
async def third_state_func(msg):
    if msg.text == '1':
        await msg.answer('Вы находитесь в гардеробе', reply_markup=first_state_keyboard)
        await Room_State.room_1.set()
    elif msg.text == '4':
        await msg.answer('В данном зале представлены древние осколки', reply_markup=fourth_state_keyboard)
        await Room_State.room_4.set()
    else:
        await msg.answer('Нет такого варианта')

@dp.message_handler(state=Room_State.room_4)
async def fourth_state_func(msg):
    if msg.text == '1':
        await msg.answer('Вы находитесь в гардеробе', reply_markup=first_state_keyboard)
        await Room_State.room_1.set()
    else:
        await msg.answer('Нет такого варианта')