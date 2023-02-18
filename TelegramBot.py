def main():
	import telebot
	import BasicGenerator
	import CapchaImageGenerator
	from PIL import Image, ImageFont, ImageDraw
	from telebot import types
	import config


	bot = telebot.TeleBot("token")


	@bot.message_handler(commands=['start', 'help'])
	def send_welcome(message):
		bot.reply_to(message, "здравсвуйте {0.first_name}.Это генератор странных имен, для продолжения напишите имя и уровень странности".format(message.from_user))


	@bot.message_handler(content_types=['text'])
	def Name_print(message):
		mm = (message.text).split()
		if len(mm)==2 and mm[1].isdigit():
			try:
				b = BasicGenerator.BasicGenerator(int(mm[1]), mm[0])
				gen = b.generate_nick()
				bot.send_message(message.chat.id, gen)
				im = (CapchaImageGenerator.CapchaImageGenerator.generate_image(gen))
				bot.send_photo(message.chat.id, im)

			except:
				bot.send_message(message.chat.id, "Ошибка")

	bot.infinity_polling()

