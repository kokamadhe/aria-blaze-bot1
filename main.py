import logging
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import openai
import os

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if your key supports it
            messages=[{"role": "user", "content": message.text}],
        )
        reply = response.choices[0].message.content
        await message.reply(reply)
    except Exception as e:
        await message.reply("❌ Error: " + str(e))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


