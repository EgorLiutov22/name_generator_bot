#import
import telebot
import BasicGenerator

bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Это генератор странных имен, для продолжения напишите имя и уровень странности")

@bot.message_handler(func=lambda message: True)
def Name_print(message):
	mm = (message.text).split()
	if len(mm)==2 and mm[1].isdigit():
		b = BasicGenerator.BasicGenerator(int(mm[1]), mm[0])
		bot.send_message(message.chat.id, b.generate_nick())

bot.infinity_polling()
