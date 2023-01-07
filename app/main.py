import telebot
from telebot.types import ReplyKeyboardMarkup, ForceReply
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

@bot.message_handler(regexp='Hola')
def handle_message(message):
    bot.reply_to(message, "Holaa soy Polo que te ayudare a controlar finanzas solo escribe /finanzas y te ayudaré")

@bot.message_handler(commands=['finanzas'])
def get_finanzas(message):
    markup = ForceReply()
    msg = bot.reply_to(message, "¿En que gastaste?", reply_markup=markup)
    # bot.send_message(message, "¿En que gastaste?", reply_markup=markup)
    bot.register_next_step_handler(msg, save_name_cost)

def save_name_cost(message):
    print("message--->",message.text)
    markup = ForceReply()
    msg = bot.reply_to(message, "Cuanto gastaste?", reply_markup=markup)
    bot.register_next_step_handler(msg, save_cost)

def save_cost(message):
    bot.reply_to(message, "Se guardo tu gasto")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    print("polo is running")
    bot.infinity_polling()
    # bot.polling()