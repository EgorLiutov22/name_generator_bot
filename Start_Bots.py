from threading import Thread
import TelegramBot, Discord_Bot

Thread(target=TelegramBot.main).start()
Thread(target=Discord_Bot.main).start()
