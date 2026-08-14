import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    menu = types.KeyboardButton("📋 Меню")
    order = types.KeyboardButton("🛒 Буюртма бериш")
    address = types.KeyboardButton("📍 Манзилимиз")
    contact = types.KeyboardButton("📞 Алоқа")

    markup.add(menu, order)
    markup.add(address, contact)

    bot.send_message(
        message.chat.id,
        "🍽 OILA CAFE\n\n"
        "Ассалому алайкум! Хуш келибсиз! 😊\n"
        "Керакли бўлимни танланг:",
        reply_markup=markup
    )
@bot.message_handler(func=lambda message: message.text == "📋 Меню")
def menu(message):
    @bot.message_handler(func=lambda message: message.text == "📋 Меню")
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🍟 Fast Food", "🍢 Шашликлар")
    markup.add("🍲 Қозон кабоблар", "🔥 Грилл")
    markup.add("🍕 Пицца", "🥟 Гўштли кулчалар")
    markup.add("🌯 Гўштли рулетлар", "🥗 Салатлар")
    markup.add("🥤 Ичимликлар")
    markup.add("🔙 Орқага")

    bot.send_message(
        message.chat.id,
        "📋 Категорияни танланг:",
        reply_markup=markup
    )
    
