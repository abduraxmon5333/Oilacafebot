import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Assalomu alaykum! 🍽\n"
        "Oila Cafe botiga xush kelibsiz!\n\n"
        "Buyurtma berish uchun menyuni tanlang."
    )

bot.infinity_polling()
