import logging, os, datetime, time, pytz
from random import randint
from aiogram import Dispatcher, Bot, executor, types
from Keyboards.inline import github

TOKEN = "7108274430:AAFYuNKtM2JiIlyfHbzd6L717tAONULNx7A"

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

uz_time = pytz.timezone('Asia/Tashkent')
user = 6457971132


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("Hello <b>Omonullo Raimkulov</b>")
    while True:
        now = datetime.datetime.now(uz_time)
        if now.hour == 23 and now.minute == 45:
            for i in range(1):
                for j in range(0, randint(1, 10)):
                    d = str(i) + ' days ago'
                    with open('file.txt', 'a') as file:
                        file.write(d + '\n')
                    os.system('git add .')
                    os.system('git commit --date="' + d + '" -m "hello"')
            os.system('git push -u origin main')
            await bot.send_message(user, "Hello <b>Omonullo Raimkulov</b>")
            await bot.send_message(user, "Pushed to your github profile today", reply_markup=github)
            time.sleep(60)
        else:
            time.sleep(30)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
