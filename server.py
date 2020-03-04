from aiogram import Dispatcher, Bot, types
from aiogram.bot import api
from config import TOKEN_API

dp = Dispatcher(bot=Bot(token=TOKEN_API))

"""Начало общения с ботом"""


@dp.message_handler(commands=['start', 'help'])
async def send_help(message: types.Message):
    await message.reply(
        text='Я телеграм бот для подсчета расходов'
    )


"""Вывод категорий"""


@dp.message_handler(commands=['categories'])
async def send_categories(message: types.Message):
    pass


"""Вывод списка расходов"""


@dp.message_handler(commands=['expenses'])
async def send_expenses(message: types.Message):
    pass


"""Вывод списка доходов"""


@dp.message_handler(commands=['revenues'])
async def send_revenues(message: types.Message):
    pass


"""Вывод списка накоплений"""


@dp.message_handler(commands=['savings'])
async def send_savings(message: types.Message):
    pass


"""Вывод статистики распределения бюджета"""


@dp.message_handler(commands=['statistics'])
async def send_revenues(message: types.Message):
    pass
