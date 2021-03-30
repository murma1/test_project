
"""
Module to start our bot
"""


from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

from const import API_TOKEN

from functions import *

updater = Updater(token=API_TOKEN)

dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler('start',
                                      start))


dispatcher.add_handler(MessageHandler(Filters.text,
                                      text_msg))

dispatcher.add_handler((CallbackQueryHandler(callback=inline_reply,
                                             pattern='yes')))

updater.start_polling()