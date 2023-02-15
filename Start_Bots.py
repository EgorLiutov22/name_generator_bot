from threading import Thread
import Telegram_BOT, Discord_Bot

Thread(target=Telegram_BOT.main).start()
Thread(target=Discord_Bot.main).start()
