from logger import logger
from dotenv import load_dotenv
import os
import telebot

def start() -> None:
	load_dotenv()
	logger.debug("READING ENVIRONMENT VARIABLES")
	bot_token = os.getenv("TELEGR_TOKEN")
	logger.info("BOT CONFIGURATION")
	logger.debug(f"TELEGR_TOKEN={bot_token}")
	logger.info("BOT OBJECT INITIALISATION")
	bot = telebot.TeleBot(bot_token)
	logger.debug(bot)

	@bot.message_handler(commands=["start"])
	def msg_start(message):
		logger.info(f"{message.chat.id} -> msg:'/start'")
		bot.send_message(message.chat.id, "[ start prompt here ]")

	@bot.message_handler(commands=["ask"])
	def msg_image(message):
		logger.info(f"{message.chat.id} -> msg:'/ask'")
		bot.send_message(message.chat.id, "[ chatgpt response here ]")


	bot.polling()
