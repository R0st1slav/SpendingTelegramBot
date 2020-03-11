from aiogram import Dispatcher, Bot
from aiogram.bot import api
from bot.config import TOKEN_API
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


PATCHED_URL = "https://telegg.ru/orig/bot{token}/{method}"
setattr(api, 'API_URL', PATCHED_URL)

bot = Bot(token=TOKEN_API,)
dp = Dispatcher(bot=bot)