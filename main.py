import telebot
import keep_alive

from flask import Flask, render_template
from threading import Thread 
import os 
bot = telebot.TeleBot("5546208652:AAEsmXNbRptFwI5TRestd9Yx8O-SClaWlLQ", )


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Salom bu bot beta rejimda ishlamoqda")


app = Flask("app")

STATIC_DIR = os.path.abspath('static')

@app.route('/')
def main():
  return "working now

def run():
  app.run("0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()

if __name__ == "__main__":
  keep_alive()
  bot.infinity_polling()
