from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
button_spisok='список команд'
button_help = 'помощь'
button_start= 'Start!'

def button_help_handler(update: Update, context: CallbackContext):  # вывод сообщения и кнопка пропадает
    update.message.reply_text(
        text="It's a trap!",
        reply_markup=ReplyKeyboardRemove(),
    )
def spisok_help_handler(update: Update, context: CallbackContext):  # вывод сообщения и кнопка пропадает
    update.message.reply_text(
        text="вот список команд",
        reply_markup=ReplyKeyboardRemove(),
    )


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if update.message.text=='/start'.lower():
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_spisok),
                ],
            ],
            resize_keyboard=True
        )
        update.message.reply_text(
            text='посмотри список по кнопке ниже',
            reply_markup=reply_markup,
        )
    return spisok_help_handler(update=update,context=context)


def main():                          # start bot
    print('Start')

    updater = Updater(
        token='1393900687:AAFRG_hsPUBotc3VJF8Zsevz9iehRh-PDIY',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
