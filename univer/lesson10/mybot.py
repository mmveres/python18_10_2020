import telebot

mytoken = '1456295667:AAGO4CBpFW8l7lWAsTSiltaSPgDrVNp-UUA'
bot = telebot.TeleBot(mytoken)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    x = int(message.text)
    bot.reply_to( message, "sum = " + str(x+x) )

bot.polling()