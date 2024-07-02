import logging
from aiogram import Dispatcher, Bot, executor, types

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
