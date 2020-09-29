main_part(update=update, context='теперь к делу')

################################################
def main_part(update: Update, context: CallbackContext):
    global slovar_rus
    global slovar_eng
    for i in slovar_rus:
        slovar_rus.append(update.message.text)
        if update.message.text=='/stop':
            break
    for i in slovar_rus:
        update.message.reply_text=slovar_rus
    print(update.message.text)
    print(slovar_rus)
    print(slovo)
################################################




################################################
conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', main_part)],

        states = {
            ANSWER: [MessageHandler(Filters.text, message_handler)]
        }
    )
   dispatcher.add_handler(conv_handler)
################################################





################################################
def delete_button(update: Update, context: CallbackContext):#удаление кнопки после того как на нее нажали
    update.message.reply_text(
        text=context,
        reply_markup=ReplyKeyboardRemove(),
    )
################################################





################################################
def main():
    print('Бот запущен')
    updater = Updater(
        token='1393900687:AAFRG_hsPUBotc3VJF8Zsevz9iehRh-PDIY',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all,callback=message_handler()))
    updater.start_polling()
    updater.idle()
################################################






################################################
def message_handler(update: Update, context: CallbackContext):  # ф-я принимает сбщ. и отв на него арг-update
    text = update.message.reply_text
    update.message.reply_text(
        text='Привет, давай общаться!',
    )
    global slovo
    slovo=update.message.text
    if update.message.text == '/start':
        return update.message.reply_text(
            text='Начинаем!!!!!',
        )
    if update.message.text == '/help':
        return delete_button(update=update, context='Привет.Пока я знаю только команды:/help, /start, /end . \n Напиши одну из этих команд!')
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
        text='Привет,я Телеграм бот,пока я только учусь,и вот список команд которые я пока могу выполнять: \n /start\n /help\n /end',
        reply_markup=reply_markup
    )
    #  переход к основной части работы бота
################################################

