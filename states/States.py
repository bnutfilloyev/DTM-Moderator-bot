from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    getName = State()
    getSubject = State()
    getId = State()

    # For add result
    getIdResult = State()
    getPhotoResult = State()
    getDataResult = State()


