from logger import logger
from dotenv import load_dotenv
import os
import telebot

def start() -> None:
	load_dotenv()
	logger.debug("Reading environment variables")
	bot_token = os.getenv("TELEGR_TOKEN")
	oai_token = os.getenv("OPENAI_TOKEN")
	logger.info("Bot configuration")
	logger.debug(f"Telegram token: {bot_token}")
	logger.debug(f"OpenAI token: {oai_token}")
	logger.info("Bot object initialisation")
	bot = telebot.TeleBot(bot_token)
	logger.debug(bot)

	@bot.message_handler(commands=["start"])
	def msg_start(message):
		logger.info(f"{message.chat.id} -> msg:'/start'")
		bot.send_message(message.chat.id, "Hello")

	@bot.message_handler(commands=["image"])
	def msg_image(message):
		logger.info(f"{message.chat.id} -> msg:'/image'")
		bot.send_photo(message.chat.id, "https://psv4.userapi.com/c240331/u255340212/docs/d21/d557dc2807d4/IMG_7936.gif")

	bot.polling()
