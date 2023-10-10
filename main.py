
import telebot
from telebot import types
from telebot.types import WebAppInfo



bot = telebot.TeleBot('6606800926:AAETK4HfFVqOk-mmfMSn87gLAlriA5XiAjY')




@bot.message_handler(commands=['start', 'main'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    courier_button = types.KeyboardButton("Курьер🏃")
    client_button = types.KeyboardButton("Клиент🙋‍♂")
    markup.add(courier_button, client_button)

    # Send the message with the initial options
    bot.send_message(message.chat.id, "Выберите роль:", reply_markup=markup)


@bot.message_handler(commands=['group'])
def group(message):
    bot.send_message(message.chat.id, f'это наша группа для общения https://t.me/moscowDeliiveryBot ')




@bot.message_handler(func=lambda message: message.text in ["Курьер🏃", "Клиент🙋‍♂"])
def on_click(message):
    user_id = message.from_user.id
    if message.text == "Курьер🏃":
        # Create a keyboard markup with two courier options
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton("Легковой", web_app=WebAppInfo(url="https://google.com/"))
        button2 = telebot.types.KeyboardButton("Грузовой", web_app=WebAppInfo(url="https://google.com/"))

        markup.add(button1, button2)
        bot.send_message(user_id, "Выберите тип курьера:", reply_markup=markup)
    elif message.text == "Клиент🙋‍♂":
        # Create a keyboard markup with two client options
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton("Легковой", web_app=WebAppInfo(url="https://youtube.com/"))
        button2 = telebot.types.KeyboardButton("Грузовой", web_app=WebAppInfo(url="https://youtube.com/"))

        markup.add(button1, button2)
        bot.send_message(user_id, "Выберите тип клиента:", reply_markup=markup)
    else:
        # Handle other messages (optional)
        bot.send_message(user_id, "Извините, не понял ваш запрос. Пожалуйста, выберите опцию из меню.")



@bot.message_handler(func=lambda message: message.text in ["Аккаунт курьера", "аккаунт клиента"])
def account_setting(message):

    if message.text == "Аккаунт курьера":
        pass
    elif message.text == "аккаунт клиента":
        pass
    






bot.polling(none_stop=True)


