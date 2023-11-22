import os
import telebot
from time import sleep
from telebot.types import Message
from constants import MARKDOWN

from password_generator import generate

bot = telebot.TeleBot(os.environ['TOKEN'])


@bot.message_handler(content_types=['text'])
def handle(message: Message):
    if message.text == '/pass':
        password = generate()
        sent_message = bot.send_message(
            chat_id=message.from_user.id,
            text=f'Ваш пароль: `{password}`\nУдаление через - 5',
            parse_mode=MARKDOWN
        )
        chat_id = sent_message.chat.id
        message_id = sent_message.message_id
        for i in range(4, 0, -1):
            sleep(1)
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=f'Ваш пароль: `{password}`\nУдаление через - {i}',
                parse_mode=MARKDOWN
            )
        sleep(1)
        bot.delete_message(chat_id=chat_id, message_id=message_id)


bot.polling(none_stop=True)
