from aiogram import Bot, Dispatcher
from Token import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(config.TOKEN)
dp = Dispatcher(bot,
                storage=storage)
