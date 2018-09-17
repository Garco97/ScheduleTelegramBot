from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'Adios{}'.format(update.message.from_user.first_name))


updater = Updater('697984917:AAEPmyM3LemXq5MkEcepsrzb927Im9_wsAA')

updater.dispatcher.add_handler(CommandHandler('ello', hello))

updater.start_polling()
updater.idle


