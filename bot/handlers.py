from bot.load_all import dp
from bot.keyboard import ListOfButtons
from bot.filters import Button
from aiogram.types import Message, CallbackQuery


@dp.message_handler(commands=['start', 'help'])
async def send_start(message: Message):
    """Начало общения с ботом"""
    await message.answer(
        text='Я телеграм бот для подсчета расходов, как я могу к Вам обращаться?'
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


@dp.message_handler()
async def send_message(message: Message):
    pass