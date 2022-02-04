from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushirish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("imtihon", "Imtihonga ro'yxatdan o'tish uchun")
        ]
    )
