import telebot
import conversations
import anecdots


TOKEN = '411297683:AAGDRvzu9FCD0sviGuyA8GvdF5o2PGEJ660'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, conversations.conv_bogdan('hello'))
    # bot.register_next_step_handler(sent, hello)


@bot.message_handler(commands=['joke'])
def new_joke(message):
    bot.send_message(message.chat.id, anecdots.get_new_joke())

def hello(message):
    bot.send_message(message.chat.id, 'Привет, %s!' % message.text)


if __name__ == "__main__":
    bot.polling()




