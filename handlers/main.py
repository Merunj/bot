import time, random
from loader import dp, bot
from states.state import Timer, Dice
from aiogram.dispatcher import FSMContext
from keyboards import dice_keyboard, start_keyboard, timer_keyboard

timer_data = {
    '30 секунд': 30,
    '1 минута': 60,
    '5 минут': 300
}

@dp.message_handler(commands=['start'])
async def start_command(msg):
    await msg.answer('Привет!', reply_markup=start_keyboard.keyboard)

@dp.message_handler(commands=['timer'])
async def timer_func(msg):
    await msg.answer('Выбери время таймера', reply_markup=timer_keyboard.keyboard)
    await Timer.state1.set()

@dp.message_handler(state=Timer.state1)
async def timer_sleep(msg, state: FSMContext):
    if msg.text[0].isdigit():
        if msg.text == '1 минута':
            await msg.answer(f'Засек 1 минуту')
            end = '1 минута истекла'
        else:
            await msg.answer(f'Засек {msg.text}')
            end = f'{msg.text} истекло'
        timer_sec = timer_data[msg.text.lower()]
        while timer_sec:
            time.sleep(1)
            timer_sec-=1
        else:
            await msg.answer(end)
    elif msg.text == 'Вернуться назад':
        await state.finish()
        await msg.answer('Начальное меню', reply_markup=start_keyboard.keyboard)
    else:
        await msg.answer('Нет такого варианта')

@dp.message_handler(commands=['dice'])
async def dice_func(msg):
    await msg.answer('Выбери, какой кубик бросить', reply_markup=dice_keyboard.keyboard)
    await Dice.state1.set()

@dp.message_handler(state=Dice.state1)
async def dice_game(msg, state: FSMContext):
    if msg.text == 'Кинуть 1 шестигранный кубик':
        await msg.answer(random.randint(1, 6))
    elif msg.text == 'Кинуть 2 шестигранных кубика':
        await msg.answer(f'{random.randint(1, 6)} {random.randint(1, 6)}')
    elif msg.text == 'Кинуть 20-гранный кубик':
        await msg.answer(random.randint(1, 20))
    elif msg.text == 'Вернуться назад':
        await state.finish()
        await msg.answer('Начальное меню', reply_markup=start_keyboard.keyboard)
    else:
        await msg.answer('Нет такого варианта')