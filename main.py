import telebot
import keep_alive
bot = telebot.TeleBot("5546208652:AAEsmXNbRptFwI5TRestd9Yx8O-SClaWlLQ", )


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Salom bu bot beta rejimda ishlamoqda")

keep_alive.keep_alive()
bot.infinity_polling()
