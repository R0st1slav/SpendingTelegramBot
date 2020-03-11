from bot.load_all import bot
from aiogram import executor


async def on_shutdown(dp):
    await bot.close()


# async def on_startup(dp):
#    await bot.send_message(admin_id, "Я запущен")


if __name__ == '__main__':
    from bot.handlers import dp
    executor.start_polling(dp)