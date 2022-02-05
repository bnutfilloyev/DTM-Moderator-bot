from aiogram import types
from aiogram.dispatcher import FSMContext

from data.text import text
from loader import dp
from states.States import Form
from utils.db_api.mongo import user_db


@dp.message_handler(commands=['add_result'], state='*')
async def add_result(msg: types.Message):
    await msg.answer(text['result_id'])
    await Form.getIdResult.set()


@dp.message_handler(content_types='text', state=Form.getIdResult)
async def get_id(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = msg.text
        await msg.answer(text['get_photo'])
        await Form.getPhotoResult.set()


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=Form.getPhotoResult)
async def get_photo(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo_id'] = msg.photo[-1].file_id
        await msg.answer(text['result_data'])
        await Form.getDataResult.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Form.getDataResult)
async def get_data(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = msg.text
        await msg.answer_photo(photo=data['photo_id'], caption=data['info'])
        user_db.update_one({'id': data['id']}, {
            "$set": {
                'photo_id': data['photo_id'],
                'info': data['info'],
            }
        })
        await state.finish()