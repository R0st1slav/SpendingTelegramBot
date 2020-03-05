from aiogram import Dispatcher, Bot, executor
from aiogram.bot import api
from config import TOKEN_API
from aiogram.types import Message, CallbackQuery
import logging
from keyboard import ListOfButtons
from filters import Button


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


PATCHED_URL = "https://telegg.ru/orig/bot{token}/{method}"
setattr(api, 'API_URL', PATCHED_URL)

dp = Dispatcher(bot=Bot(token=TOKEN_API,))

keyboard = ListOfButtons(text=["день", "месяц", "год"],
                         callback=["1", '2', '3'],
                         align=[3]).inline_keyboard


@dp.message_handler(commands=['start', 'help'])
async def send_start(message: Message):
    """Начало общения с ботом"""
    await message.answer(
        text='Я телеграм бот для подсчета расходов'
    )


@dp.message_handler(commands=['categories'])
async def send_categories(message: Message):
    """Вывод категорий"""
    pass


@dp.message_handler(commands=['expenses'])
async def send_expenses(message: Message):
    """Вывод списка расходов"""
    await message.answer('Выберите период за который показать расходы: ', reply_markup=keyboard)


@dp.message_handler(commands=['incomes'])
async def send_revenues(message: Message):
    """Вывод списка доходов"""
    await message.answer('Выберите период за который показать доходы: ', reply_markup=keyboard)


@dp.message_handler(commands=['savings'])
async def send_savings(message: Message):
    """Вывод списка накоплений"""
    await message.answer('Выберите период за который показать накопления: ', reply_markup=keyboard)


@dp.message_handler(commands=['statistics'])
async def send_revenues(message: Message):
    """Вывод статистики распределения бюджета"""
    pass


@dp.callback_query_handler(Button("1"))
async def filter_period(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("test")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)