from logger import logger
from dotenv import load_dotenv
import os
import telebot

def start() -> None:
	load_dotenv()
	logger.debug("READING ENVIRONMENT VARIABLES")
	bot_token = os.getenv("TELEGR_TOKEN")
	oai_token = os.getenv("OPENAI_TOKEN")
	logger.info("BOTT CONFIGURATION")
	logger.debug(f"TELEGR_TOKEN={bot_token}")
	logger.debug(f"OPENAI_TOKEN={oai_token}")
	logger.info("BOT OBJECT INITIALISATION")
	bot = telebot.TeleBot(bot_token)
	logger.debug(bot)

	@bot.message_handler(commands=["start"])
	def msg_start(message):
		logger.info(f"{message.chat.id} -> msg:'/start'")
		bot.send_message(message.chat.id, "Hello")

	@bot.message_handler(commands=["image"])
	def msg_image(message):
		logger.info(f"{message.chat.id} -> msg:'/image'")
		if (os.path.exists("source\content\image.gif") == False):
			logger.warning("UNABLE TO FIND IMAGE FILE")
			bot.send_massage(message.chat.id, "Unable to load image :(")
		else:
			bot.send_photo(message.chat.id, photo=open("source\content\image.gif", "rb"))

	bot.polling()
