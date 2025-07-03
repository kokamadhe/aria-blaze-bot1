from aiogram import Bot, Dispatcher, types, executor
import openai
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Configure logging
logging.basicConfig(level=logging.INFO)

# OpenAI setup
openai.api_key = OPENAI_API_KEY

# Start command
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply("🔥 Hello! I’m Aria Blaze. Send me a message and I’ll seduce you with AI magic...")

# Handle messages
@dp.message_handler()
async def handle_message(message: types.Message):
    user_input = message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are Aria Blaze, a flirtatious and seductive AI girl."},
                {"role": "user", "content": user_input}
            ]
        )

        reply_text = response.choices[0].message.content.strip()
        await message.reply(reply_text)

    except Exception as e:
        await message.reply("⚠️ Something went wrong: " + str(e))

# Run bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

