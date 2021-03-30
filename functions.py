
"""
Module with functions
"""

import datetime

import messages as msg

import answers_dicts as ans

import markups as mrk

from telegram.constants import CHATACTION_TYPING

import time


def start(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = msg.ru_hello.format(first_name)
    context.bot.send_message(chat_id=chat_id,
                             text=text)


def text_msg(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = update.message.text.lower()

    if text == 'к1':
        context.bot.send_message(chat_id=chat_id,
                                 reply_markup=mrk.inline_button(),
                                 text='Кнопка нажата! Выберите другую ниже')
    
    else:
        send_text = ans.global_answers['rus'][text].format(first_name)

        context.bot.send_message(chat_id=chat_id,
                                 text=send_text,
                                 reply_markup=mrk.button())


def inline_reply(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    text = update.callback_query.message.text.lower()

    context.bot.send_chat_action(chat_id=chat_id,
                                 action=CHATACTION_TYPING)
    context.bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
    context.bot.send_message(chat_id=chat_id,
                              text='okay')

def photo_msg(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    photo_id = update.message.photo[-1].file_id

    f = context.bot.get_file(photo_id)
    t = datetime.datetime.now().timestamp()
    f.download('photos/{}.jpg'.format(str(chat_id) + str(t)))