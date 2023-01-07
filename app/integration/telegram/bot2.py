import telebot
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN_TELEGRAM")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def enviar(message):
    bot.reply_to(message, "Hola, soy un bot que te ayudará a encontrar")

@bot.message_handler(commands=['hola'])
def send_welcome(message):
    print("message--->",message.text)
    bot.reply_to(message, "que ondaaa")

@bot.message_handler(regexp="Hola")
def handle_message(message):
    bot.reply_to(message, "Que ongo con tu uña")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
