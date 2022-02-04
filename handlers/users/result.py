from aiogram import types

from data.text import text
from loader import dp
from utils.db_api.mongo import user_db


@dp.message_handler(content_types=["text"])
async def get_id(message: types.Message):
    id = message.text
    metadata = user_db.find_one({'id': id})
    try:
        if metadata != None:
            await message.answer_photo(photo=metadata['photo_id'], caption=text['result'].format(
                id,
                metadata['subject'],
                metadata['locate'],
                metadata['info'],
            ))
        else:
            await message.answer(text['not_found'])
    except:
        await message.answer(text['error'])