import logging
from aiogram import Dispatcher, Bot, executor, types
from Keyboards.inline import github

TOKEN = "7108274430:AAFYuNKtM2JiIlyfHbzd6L717tAONULNx7A"

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("Hello <b>Omonullo Raimkulov</b>")

    await message.answer("Pushed to your github profile today", reply_markup=github)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
