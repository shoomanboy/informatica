from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler, CommandHandler, ConversationHandler, RegexHandler
from telegram import KeyboardButton, ChatMember, Chat, Contact
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
import googletrans
from googletrans import Translator
# update.message.text-сообщение введеное человеком боту
# update.message.reply_text-сообщение выведеное на экран
# reply_markup-Встроенная клавиатура, прикрепленная к сообщению.
#
slovo = 0
button_stop = '/stop'  # кнопка stop
button_help = '/help'  # кнопка help
button_start = '/translate'  # кнопка start
button_end = '/end'  # кнопка end
slovar_rus = []  # массив запоминающий введеные русские слова после /start
slovar_eng = []  # массив запоминающий перевод слов



def message_handler(update: Update, context: CallbackContext):
    my_keyboard = ReplyKeyboardMarkup([[button_start], [button_help],[button_end]])
    update.message.reply_text(
        text="Привет %s, давай общаться! \n Нажми на одну из кнопок. \n Кнопка '/translate' запустит переводчик\n Кнопка '/help' подскажет тебе что делать\n Кнопка '/end' завершит работу" %(format(update.message.chat.first_name)),
        reply_markup=my_keyboard
    )



def delete_button(update: Update, context: CallbackContext):  # удаление кнопки после того как на нее нажали
    update.message.reply_text(
        text=context,
        reply_markup=ReplyKeyboardRemove()
    )
    #  переход к основной части работы бота


def main_part(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Translator\n Введите слово',
        reply_markup=ReplyKeyboardRemove(),
    )
    global slovar_rus
    global slovar_eng
    return"stop"

def message_stop(update: Update, context: CallbackContext):
    my_keyboard = ReplyKeyboardMarkup([[button_start], [button_help],[button_end]])
    translator = Translator()
    slovo=update.message.text
    perevod=translator.translate(slovo)
    update.message.reply_text(text='%s-%s'%(slovo,perevod.text),reply_markup=my_keyboard)
    update.message.reply_text(text='Выбери команду')
    return "menu"



def message_end(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='До скорой встречи\n Надеюсь ты все запомнил!',
        reply_markup=ReplyKeyboardRemove(),
    )


def message_help(update: Update, context: CallbackContext):
    my_keyboard = ReplyKeyboardMarkup([[button_start], [button_help], [button_end]])
    update.message.reply_text(
        text="Я знаю пока три команды:'перевод', '/help', '/end'",
        reply_markup=my_keyboard
    )


def main():
    print('Бот запущен')
    updater = Updater(
        token='1393900687:AAFRG_hsPUBotc3VJF8Zsevz9iehRh-PDIY',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('start|/start|привет|Привет|Start'),message_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('/help'), message_help))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('/end'), message_end))
    updater.dispatcher.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('/translate'), main_part)],
                            states={
                                "stop":[MessageHandler(Filters.all,message_stop)],
                                "menu":[MessageHandler(Filters.all,message_handler)]
                            },
                            fallbacks=[MessageHandler(Filters.regex('/translate'), main_part)]
                            )
    )
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
