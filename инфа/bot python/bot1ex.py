from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler, CommandHandler, ConversationHandler, RegexHandler
from telegram import KeyboardButton, ChatMember, Chat, Contact
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

# update.message.text-сообщение введеное человеком боту
# update.message.reply_text-сообщение выведеное на экран
# reply_markup-Встроенная клавиатура, прикрепленная к сообщению.
#
slovo = 0
button_stop = '/stop'  # кнопка stop
button_help = '/help'  # кнопка help
button_start = '/start'  # кнопка start
button_end = '/end'  # кнопка end
slovar_rus = []  # массив запоминающий введеные русские слова после /start
slovar_eng = []  # массив запоминающий перевод слов


def delete_button(update: Update, context: CallbackContext):  # удаление кнопки после того как на нее нажали
    update.message.reply_text(
        text=context,
        reply_markup=ReplyKeyboardRemove(),
    )


def message_handler(update: Update, context: CallbackContext):  # ф-я принимает сбщ. и отв на него арг-update
    text = update.message.reply_text
    global slovo
    slovo = update.message.text
    if update.message.text == '/start':
        return update.message.reply_text(
            text='Начинаем!!!!!',
        )
    if update.message.text == '/help':
        return delete_button(update=update,
                             context='Привет.Пока я знаю только команды:/help, /start, /end . \n Напиши одну из этих команд!')
    if update.message.text == '/end':
        return delete_button(update=update, context='Жаль что ты уходишь, до скорой встречи!')
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
        text='Привет %s,я Телеграм бот,пока я только учусь,и вот список команд которые я пока могу выполнять: \n /start\n /help\n /end'%(format(update.message.chat.first_name)),
        reply_markup=reply_markup
    )
    #  переход к основной части работы бота


def main_part(update: Update):
    while update.message.text!='/stop':
        global slovar_rus
        global slovar_eng
        slovar_rus.append(update.message.text)
        if update.message.text == '/stop':
            for i, item in enumerate(slovar_rus):
                b = item
                if b == '/stop':
                    break
                update.message.reply_text(
                    text=b
                )
            update.message.reply_text(
                text='Ты молодец!!!',
            )




def main():
    print('Бот запущен')
    updater = Updater(
        token='1393900687:AAFRG_hsPUBotc3VJF8Zsevz9iehRh-PDIY',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(Filters.all,message_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('/start'),main_part))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('/stop'),message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
