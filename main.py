import logging
from checkWord import checkWord
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5767461003:AAHT9nMDOHYjrXQRUK2nSQRbZhe5yetJPZw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("imloSami botiga xush kelibsiz!!!!!")

@dp.message_handler(commands=['help'])
async def help_user(message: types.Message):
    await message.reply("imloSami botdan foydalanish uchun so'z yuboring")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
