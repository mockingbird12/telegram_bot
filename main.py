import telebot
import conversations
import anecdots
import random
import time


TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, conversations.conv_bogdan('hello'))
    # bot.register_next_step_handler(sent, hello)


@bot.message_handler(regexp='шутк')
def hello(message):
    bot.send_message(message.chat.id, conversations.conv_bogdan('intro'))
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, anecdots.get_new_joke())
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(4)
    pictures = ['badumts1.jpeg', 'badumts2.jpeg', 'badumts3.jpeg']
    msg = bot.send_photo(message.chat.id, open('images/' + pictures[random.randint(0, len(pictures))], 'rb'), None)
    # bot.send_message(message.chat.id, msg.photo[1].file_id, reply_to_message_id=msg.message_id)


if __name__ == "__main__":
    bot.polling()




