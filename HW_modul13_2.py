from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio 

API = ""
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start']) #Хэндлер для реагирования на команды
async def start_message(message):
    print(f"Привет!, {message.from_user.username}.  Я бот помогающий твоему здоровью.")  

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
