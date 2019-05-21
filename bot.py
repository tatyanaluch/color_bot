from variables import *
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext import Filters
import color
import logging
import images
import color_names


updater = Updater(token=TOKEN, request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    update.message.reply_text('''
    Hi! I'm Сolor Bot.
    You can send me HEX, RGB, RGB float and color name.
    And I try to transform it.''')


def handle_text_message(bot, update):
    message_text = update.message.text
    try:
        color_int, exact = parse_color(message_text)
        color_info = '''
<b>HEX</b>: {}
<b>RGB</b>: {}
<b>RGB</b> float: {}
        '''.format(
            color.print_hex_color(color_int),
            color.print_rgb_int_color(color_int),
            color.print_rgb_float_color(color_int)
        )

        color_name = color_names.find_color_name(color_int)
        if color_name is not None:
            if exact:
                color_info = "<b>'{}'</b>\n{}".format(color_name, color_info)
            else:
                color_info = "Maybe you meant <b>'{}'</b>\n{}".format(color_name, color_info)

        stream = images.create_solid_image_stream(color_int)

        bot.send_photo(
            update.message.chat_id,
            photo=stream,
            caption=color_info,
            parse_mode='html'
        )

    except TypeError:
        update.message.reply_text("Sorry, but I don't know color '{}'".format(message_text))


def handle_any_message(bot, update):
    update.message.reply_text("I don't know what you want, but please send me a color:)")


def parse_color(text):
    result = color.parse_hex_color(text)
    if result is None:
        result = color.parse_rgb_color(text)
        if result is None:
            color_and_similarity_by_name = color_names.find_color_by_name(text)

            if color_and_similarity_by_name is not None:
                color_by_name, similarity = color_and_similarity_by_name
                return color.parse_hex_color(color_by_name), similarity == 1

    return result, True


start_handler = CommandHandler('start', start)
text_message_handler = MessageHandler(Filters.text, handle_text_message)
any_message_handler = MessageHandler(Filters.photo, handle_any_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(any_message_handler)


updater.start_polling()
