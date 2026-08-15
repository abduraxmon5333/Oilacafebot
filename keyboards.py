from telebot import types
from keyboards import main_menu
from config import CAFE_NAME


def register_handlers(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(
            message.chat.id,
            f"🍽 {CAFE_NAME}\n\n"
            "Ассалому алайкум!\n"
            "Қуйидаги менюдан керакли бўлимни танланг.",
            reply_markup=main_menu()
        )
