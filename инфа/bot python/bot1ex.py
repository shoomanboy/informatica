from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton, ChatMember, Chat, Contact
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

# update.message.text-сообщение введеное человеком боту
# update.message.reply_text-сообщение введеное ботом
# reply_markup-Встроенная клавиатура, прикрепленная к сообщению.
#

button_help = '/help'
button_start = '/start'
button_end = '/end'


def delete_button(update: Update,context:CallbackContext):
    update.message.reply_text(
        text=context,
        reply_markup=ReplyKeyboardRemove(),
    )


def message_handler(update: Update, context: CallbackContext):  # ф-я принимает сбщ. и отв на него арг-update
    text = update.message.reply_text
    if update.message.text == '/start':
        return delete_button(update=update, context='привет,давай общаться.\n Введи мне слово или предложение!')
    if update.message.text == '/help':
        return delete_button(update=update, context='Привет.Пока я знаю только команды:/help, /start, /end . \n Напиши одну из этих команд!')
        reply_markup=reply_markup
    if update.message.text == '/end':
        return delete_button(update=update,context='Жаль что ты уходишь, до скорой встречи!')

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_start),
                KeyboardButton(text=button_help),
                KeyboardButton(text=button_end),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text='Привет,я Телеграм бот,пока я только учусь,и вот список команд которые я пока могу выполнять: \n /start\n /help\n /end',
        reply_markup=reply_markup
    )


def main():
    print('start')
    updater = Updater(
        token='1393900687:AAFRG_hsPUBotc3VJF8Zsevz9iehRh-PDIY',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
