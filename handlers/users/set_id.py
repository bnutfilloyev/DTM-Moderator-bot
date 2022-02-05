from aiogram import types
from aiogram.dispatcher import FSMContext

from data.text import text
from loader import dp
from states.States import Form
from utils.db_api.mongo import user_db


@dp.message_handler(commands=['imtihon'], state="*")
async def imtihon(message: types.Message):
    await message.answer(text['get_name'])
    await Form.getName.set()


@dp.message_handler(content_types='text', state=Form.getName)
async def get_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
        await msg.answer(text['get_subject'])
        await Form.getSubject.set()


@dp.message_handler(content_types='text', state=Form.getSubject)
async def get_subject(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['subject'] = msg.text
        await msg.answer(text['get_id'])
        await Form.getId.set()


@dp.message_handler(content_types='text', state=Form.getId)
async def get_subject(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = msg.text
        metadata = user_db.find_one({'id': data['id']})

        if metadata == None:
            count = user_db.count()
            user_db.insert({
                'id': data['id'],
                'name': data['name'],
                'subject': data['subject'],
                'locate': count,
            })
        else:
            count = metadata['locate']

        await msg.answer(text['set_id'].format(data['name'], data['subject'], data['id'], count))
        await state.finish()
