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
slovo = 0  # переменная в которую будет сохраняться введеное предложение
button_stop = '/stop'  # кнопка stop
button_help = '/help'  # кнопка help
button_start = '/translate'  # кнопка start
button_start_again='/translate_again'
button_end = '/end'  # кнопка end
slovar_rus = []  # массив запоминающий введеные русские слова после /start
slovar_eng = []  # массив запоминающий перевод слов



def message_handler(update: Update, context: CallbackContext):#Запуск бота,самый первый шаг
    my_keyboard = ReplyKeyboardMarkup([[button_start], [button_help],[button_end]])
    update.message.reply_text(
        text="Привет %s, давай общаться! \n Нажми на одну из кнопок. \n Кнопка '/translate' запустит переводчик\n Кнопка '/help' подскажет тебе что делать\n Кнопка '/end' завершит работу" %(format(update.message.chat.first_name)),
        reply_markup=my_keyboard
    )

def dontknow(update:Update,context:CallbackContext):#Если непривально введена команда,то будет отправляться пользователю данная команда
    update.message.reply_text(text='Я вас не понимаю,нажмите на команду')


def main_part(update: Update, context: CallbackContext):#После нажатия кнопки /translate запускается диалог с переводчиком
    update.message.reply_text(
        text='Translator\n Введите слово',
        reply_markup=ReplyKeyboardRemove(),
    )
    global slovo
    global slovar_rus
    global slovar_eng
    return"message stop"

def message_stop(update: Update, context: CallbackContext):#Здесь обрабатывается полученное сообщение,слово переводится и отправляется пользователю
    translator = Translator()
    slovo = update.message.text
    perevod = translator.translate(slovo)
    update.message.reply_text(text='%s-%s\n' % (slovo, perevod.text))
    my_keyboard = ReplyKeyboardMarkup([[button_start_again], [button_help], [button_end]])
    update.message.reply_text(text='выбери команду',reply_markup=my_keyboard)
    return "road"


def road(update:Update,context:CallbackContext):
    if update.message.text==button_start_again:#запуск переводчика
        update.message.reply_text(text='Введите слово',reply_markup=ReplyKeyboardRemove())
        return"message stop"
    elif update.message.text==button_help:        #запуск меню /help
        return message_help
    elif update.message.text==button_end:        #закончить диалог с ботом
        return message_end


def message_end(update: Update, context: CallbackContext):#Заканчиваем диалог с ботом по команде /end
    update.message.reply_text(
        text='До скорой встречи\n Надеюсь ты все запомнил!\nЕсли захочешь пообщаться, то напиши команду /translate_again',
        reply_markup=ReplyKeyboardRemove(),
    )




def message_help(update: Update, context: CallbackContext):#Пользователю высвечиивается список доступных команд по нажатию кнопки /help
    my_keyboard = ReplyKeyboardMarkup([[button_start_again], [button_help], [button_end]])
    update.message.reply_text(text="Я знаю пока три команды:'/translate_again', '/help', '/end'",reply_markup=my_keyboard)
    return "road"

def main():#Основные параметры бота(токен,обработчики сообщений и команд,и обработчик определенного диалога
    print('Бот запущен')
    updater = Updater(
        token='1393900687:AAFRG_hsPUBotc3VJF8Zsevz9iehRh-PDIY',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('/help'), message_help))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('/end'), message_end))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('start|/start|привет|Привет|Start'),message_handler))
    updater.dispatcher.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('/translate'), main_part)],
                            states={
                                "message stop":[MessageHandler(Filters.all,message_stop)],
                                "road":[MessageHandler(Filters.regex('/translate_again|/help|/end'),road)]
                            },
                            fallbacks=[]
                            )
    )
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
