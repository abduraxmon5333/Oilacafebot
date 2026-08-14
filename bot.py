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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🍟 Fast Food", "🍢 Шашликлар")
    markup.add("🍲 Қозон кабоблар", "🔥 Грилл")
    markup.add("🍕 Пицца", "🥟 Гўштли кулчалар")
    markup.add("🌯 Гўштли рулетлар", "🥗 Салатлар")
    markup.add("🥤 Ичимликлар", "🔙 Орқага")

    bot.send_message(@bot.message_handler(func=lambda message: message.text == "🍟 Fast Food")
def fast_food(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🍔 Бургерлар", "🌯 Лаваш")
    markup.add("🍟 Фри", "🍗 KFS")
    markup.add("🍕 Пицца", "🌭 Хот-дог")
    markup.add("🔙 Орқага")

    bot.send_message(@bot.message_handler(func=lambda message: message.text == "🍟 Fast Food")
def fast_food(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🍔 Бургерлар", "🌯 Лаваш")
    markup.add("🍟 Фри", "🍗 KFS")
    markup.add("🍕 Пицца", "🌭 Хот-дог")
    markup.add("🔙 Орқага")

    bot.send_message(
        message.chat.id,
        "🍟 Fast Food:",
        reply_markup=markup
    )
        message.chat.id,
        "🍟 Fast Food:",
        reply_markup=markup     bot.send_message(
        message.chat.id,
        "🍟 Fast Food:",
        reply_markup=markup
            @bot.message_handler(func=lambda message: message.text == "🍔 Бургерлар")
def burgerlar(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🍔 Товуқли — 15 000 сўм")
    markup.add("🍔 Мол — 20 000 сўм")
    markup.add("🔙 Орқага")

    bot.send_message(
        message.chat.id,
        "🍔 Бургер турини танланг:",
        reply_markup=markup
    )
    )
@bot.@bot.message_handler(func=lambda message: message.text == "🌯 Лаваш")
def lavash(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🌯 Товуқли — 20 000 сўм")
    markup.add("🌯 Гўштли — 30 000 сўм")
    markup.add("🔙 Орқага")

    bot.send_message(
        message.chat.id,
        "🌯 Лаваш турини танланг:",
        reply_markup=markup
    )
@bot.message_handler(func=lambda message: message.text == "🌭 Хот-дог")
def hotdog(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🌭 Оддий — 10 000 сўм")
    markup.add("🌭 Хот-дог — 15 000 сўм")
    markup.add("🌭 Биг Хот-дог — 20 000 сўм")
    markup.add("🔙 Орқага")

    bot.send_message(
        message.chat.id,
        "🌭 Хот-дог турини танланг:",
        reply_markup=markup
    )
    )
@bot.message_handler(func=lambda message: message.text == "🍟 Фри")
def fri(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🍟 Фри — 15 000 сўм")
    markup.add("🔙 Орқага")

    bot.send_message(
        message.chat.id,
        "🍟 Фри:",
        reply_markup=markup
                    )
@
    )
@bot.message_handler(func=lambda message: message.text == "🍗 KFC")
def kfc(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🍗 KFC — 30 000 сўм")
    markup.add("🔙 Орқага")

    bot.send_message(
        message.chat.id,
        "🍗 KFC:",
        reply_markup=markup
    )
    @bot.message_handler(func=lambda message: message.text == "🍕 Пицца")
def pizza(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("🍕 Маргарита — 30 см — 45 000 сўм")
    markup.add("🍕 Пепперони — 30 см — 45 000 сўм")
    markup.add("🍕 Товуқли — 30 см — 45 000 сўм")
    markup.add("🍕 Гўштли — 35 см — 50 000 сўм")
    markup.add("🔙 Орқага")

    bot.send_message(
        message.chat.id,
        "🍕 Пицца турини танланг:",
        reply_markup=markup
)
        message.chat.id,
        "📋 Категорияни танланг:",
        reply_markup=markup
    )      
    
        
    )


@bot.message_handler(func=lambda message: message.text == "🛒 Буюртма бериш")
def order(message):
    bot.send_message(
        message.chat.id,
        "🛒 Буюртма бериш бўлими тез орада ишлайди."
    )


@bot.message_handler(func=lambda message: message.text == "📍 Манзилимиз")
def address(message):
    bot.send_message(
        message.chat.id,
        "📍 OILA CAFE\n\nМанзилимиз тез орада қўшилади."
    )


@bot.message_handler(func=lambda message: message.text == "📞 Алоқа")
def contact(message):
    bot.send_message(
        message.chat.id,
        "📞 Алоқа\n\nТелефон рақамимиз тез орада қўшилади."
    )


bot.infinity_polling()
