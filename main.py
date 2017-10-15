import telebot


TOKEN = '411297683:AAGDRvzu9FCD0sviGuyA8GvdF5o2PGEJ660'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Привет, %s!' % message.text)


bot.polling()




