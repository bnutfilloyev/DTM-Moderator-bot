from aiogram import types

from data.text import text
from loader import dp
from states.States import Form


@dp.message_handler(commands=['add_result'])
async def add_result(msg: types.Message):
    await msg.answer(text['get_photo'])
    await Form.getPhoto.set()


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=Form.getPhoto)
async def get_photo(msg: types.Message):
    photo = msg.photo[-1]
    await msg.answer(photo.as_json())
