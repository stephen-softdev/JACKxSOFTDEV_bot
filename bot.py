import schedule
import time
from telegram import Bot
import os
import random
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = "@JACKxSOFTDEV"
IMAGE_PATH = "poster.jpg"

bot = Bot(token=TOKEN)

caption = """⭐ Professional Website Development
👉 DM pannunga @Win_jackpo

💡 Business Website | Portfolio | E-commerce
⚡ Web Development Course
🤖 Telegram Bot & Automation
📽️ Project Work
🎨 Video & Photo Editing

🔥 LIMITED OFFER
First 10 clients ku 50% OFF 💸

📩 Contact: @Win_jackpo
"""

# 👇 async function
async def send_post():
    with open(IMAGE_PATH, 'rb') as photo:
        await bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=caption)

# 👇 wrapper for schedule
def job():
    asyncio.run(send_post())

schedule.every().day.at("08:00").do(job)
schedule.every().day.at("20:00").do(job)

print("Bot running... 🚀")

# 🔥 quick test
job()

while True:
    schedule.run_pending()
    time.sleep(1)

async def auto_react(update: Update, context: ContextTypes.DEFAULT_TYPE):
    emojis = ["🔥", "❤️", "👍", "😎", "🚀", "💯"]

    for i in range(4):  # 👈 number of reactions (4 times)
        await update.message.reply_text(random.choice(emojis))
        await asyncio.sleep(1)  # delay (natural feel)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, auto_react))

print("Bot running... 🚀")
app.run_polling()