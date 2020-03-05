from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery


class Button(BoundFilter):
    def __init__(self, key):
        self.key = key

    async def check(self, message) -> bool:
        if isinstance(message, Message):
            return message.text == self.key
        elif isinstance(message, CallbackQuery):
            return self.key == message.data
