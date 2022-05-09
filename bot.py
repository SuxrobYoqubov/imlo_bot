import logging
from imlo import get_close_matches, checkWord

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5339972860:AAGOh2CX4x20mXxxMCzxYBFZBY-XEv7qZg4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("O'zbek imlolari botiga xush kelibsiz")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):

    await message.reply("Botdan foydalanish uchun so'z yuboring")



@dp.message_handler()
async def imlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)