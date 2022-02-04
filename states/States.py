from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    getPhoto = State()
    getData = State()