import telebot

from telebot import types

token = "7782281184:AAH2TlidsvuQVtVtj7UyUDHtAdXU-zhp6aM"
bot = telebot.TeleBot(token=token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Главное меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Информация обо мне")
    button2 = types.KeyboardButton("Мои проекты")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, "Салют! Выберите опцию:", reply_markup=markup)

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_menu(message):
    if message.text == "Информация обо мне":
        # Подменю для "Информация обо мне"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button3 = types.KeyboardButton("Биография")
        button4 = types.KeyboardButton("Образование")
        button5 = types.KeyboardButton("Назад в главное меню")
        markup.add(button3, button4, button5)
        bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

    elif message.text == "Мои проекты":
        # Отправляем ссылку на бот
        bot.send_message(message.chat.id, "Мой проект: https://t.me/vcard_tehnikum_bot")

    elif message.text == "Биография":
        # Отправляем информацию о пользователе
        bot.send_message(message.chat.id, "Имя: Равшан\nФамилия: Ишимов\nВозраст: 38\nПол: Мужской")

    elif message.text == "Образование":
        # Отправляем информацию об образовании
        bot.send_message(message.chat.id, "Образование: Tehnikum school")

    elif message.text == "Назад в главное меню":
        # Возвращаемся в главное меню
        start(message)

# Цикл
bot.infinity_polling()