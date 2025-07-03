import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        user_input = message.text

        # Use new OpenAI syntax
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a flirty, sexy, naughty chatbot named Aria Blaze."},
                {"role": "user", "content": user_input}
            ]
        )

        reply_text = response.choices[0].message.content
        await message.answer(reply_text)

    except Exception as e:
        await message.answer("Oops! Something went wrong.")
        logging.exception(e)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)



