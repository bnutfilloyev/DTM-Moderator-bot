from loader import dp


@dp.message_handler(content_types=["text"])
async def get_id(message):
    await message.answer(message.from_user.id)
