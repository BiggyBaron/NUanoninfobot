#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2019"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"

import telebot
from telebot import types
import logging
import datetime
import time
import urllib


# region: Данные для бота
token = "1443772682:AAEX8JqFuKpZAIbkXD-0w5l83iRHWK2AT1w"
bot = telebot.TeleBot("1443772682:AAEX8JqFuKpZAIbkXD-0w5l83iRHWK2AT1w")
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
group_id = "-441572523"
log_group = "-252679315"
# endregion


def copy_msg(message):
    url = 'https://api.telegram.org/bot' + token + "/copyMessage?chat_id=" + group_id + "&from_chat_id=" + str(message.chat.id) + "&message_id=" + str(message.message_id)
    f = urllib.request.urlopen(url)


# Приветсвие
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    hello_string = '''Hello!\nMy name is AnonInfo🤖, I help you to anonymously report🧐 a problem on the campus of Nazarbayev University🏛.\n
To send an anonymous report📄, just send me what happened and where happened. There is an example:\n
<code>
Somebody brake window in the 7th block on the 2nd floor near the 212th room.
</code>
You can attach a photo or video to the report by sending me them.\n\n
Thank you for your time!\n\n
I am here to improve our lives at Nazarbayev University🏛!'''
    bot.send_message(message.chat.id, hello_string, parse_mode="html")


@bot.message_handler(content_types=['text'])
def text_handler(message):

    bot.forward_message(log_group, message.chat.id, message.message_id)
    
    log_m = {
        "from": str(message.chat.id),
        "time": message.date,
        "message": message.text
        }
    
    msg = "<b>New report!</b>\nDate: " + str(message.date) + "\nText:\n<code>" + str(message.text) + "</code>"
    bot.send_message(group_id, msg, parse_mode="html")

    msg2 = "Thank you for your help!\nReport is received!"
    bot.send_message(message.chat.id, msg2)


@bot.message_handler(content_types=['audio', 'document', 'photo', 'video', 'voice', 'video_note'])
def text_handler2(message):

    bot.forward_message(log_group, message.chat.id, message.message_id)
    
    log_m = {
        "from": str(message.chat.id),
        "time": message.date,
        "message": message.text
        }
    
    msg = "<b>New report!</b>\nDate: " + str(message.date) + "\nText:\n<code>" + str(message.text) + "</code>"
    copy_msg(message)

    msg2 = "Thank you for your help!\nReport is received!"
    bot.send_message(message.chat.id, msg2)


if __name__ == "__main__":
    bot.polling(none_stop=True)

