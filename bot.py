import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

from handlers import register_handlers

bot = telebot.TeleBot(TOKEN)

register_handlers(bot)

print("Bot ishga tushdi...")

bot.infinity_polling(skip_pending=True)
