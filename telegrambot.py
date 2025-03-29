import telebot
import imgkit
from telebot import types
from html2image import Html2Image

from functions import get_replacement_html
from functions import save_html_to_file

from scraper import get_replacement

TOKEN = '6684374207:AAEDoqYI64rswZA1q3JYR93ugo5XCTb78Tk'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item_3 = types.KeyboardButton("Заміни")
    markup.add(item_3)

    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Заміни")
def send_replacement(message):
    data = get_replacement()
    html = get_replacement_html(data)
    save_html_to_file(html)

    # imgkit.from_file('Заміни.html', 'Заміни.jpeg')

    with open("Заміни.html", "rb") as file:
        bot.send_document(message.chat.id, file)

    # with open("Заміни.jpeg", "rb") as photo:
    #     bot.send_photo(message.chat.id, photo)
    hti = Html2Image()
    hti.size = (600, 1000)
    hti.screenshot(html_str=html, save_as='page.png')

    with open("page.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo)






@bot.message_handler(commands=['hello'])
def greet_user(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Привіт, {user_name}!")


bot.polling()
