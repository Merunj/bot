from aiogram.dispatcher.filters.state import StatesGroup, State

class Room_State(StatesGroup):
    room_1 = State()
    room_2 = State()
    room_3 = State()
    room_4 = State()
    start_museum = State()