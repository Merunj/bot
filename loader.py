#Инициализация бота

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import logging

bot = Bot('6065397450:AAGyt7sKGBgTVn3kPMF8f9uklCLglcH_6UA')
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(
    level=logging.INFO, 
    format= '[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


