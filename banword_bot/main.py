import re
import logging
from os import environ
import telebot
from .const import BANNED_REGEX

bot = telebot.TeleBot(environ.get("BANWORDBOT_TOKEN"))


@bot.message_handler(content_types=["text"])
def handle_messages(message):
    for r in BANNED_REGEX:
        logging.debug(r)
        if re.search(r, message.text):
            logging.info(message.text)
            bot.delete_message(message.chat.id, message.message_id)


def bot_main():
    bot.infinity_polling()
