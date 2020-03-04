from aiogram import Dispatcher, Bot, executor
from aiogram.bot import api
from config import TOKEN_API
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
import logging


dp = Dispatcher(bot=Bot(token=TOKEN_API))
logging.basicConfig(level=logging.INFO)


buttons = [[KeyboardButton(text='day'),
           KeyboardButton(text='month'),
           KeyboardButton(text='year')]]

period_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)


"""Начало общения с ботом"""


@dp.message_handler(commands=['start', 'help'])
async def send_start(message: Message):
    await message.answer(
        text='Я телеграм бот для подсчета расходов'
    )


"""Вывод категорий"""


@dp.message_handler(commands=['categories'])
async def send_categories(message: Message):
    pass


"""Вывод списка расходов"""


@dp.message_handler(commands=['expenses'])
async def send_expenses(message: Message):
    await message.answer('Выберите период за который показать расходы: ', reply_markup=period_markup)


"""Вывод списка доходов"""


@dp.message_handler(commands=['incomes'])
async def send_revenues(message: Message):
    await message.answer('Выберите период за который показать доходы: ', reply_markup=period_markup)


"""Вывод списка накоплений"""


@dp.message_handler(commands=['savings'])
async def send_savings(message: Message):
    await message.answer('Выберите период за который показать накопления: ', reply_markup=period_markup)


"""Вывод статистики распределения бюджета"""


@dp.message_handler(commands=['statistics'])
async def send_revenues(message: Message):
    pass


@dp.message_handler(lambda message: 'day' == message.text or 'month' == message.text or 'year' == message.text)
async def send_message(message: Message):
    if message.text is 'day':
        pass
    elif message.text is 'month':
        pass
    elif message.text is 'year':
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
