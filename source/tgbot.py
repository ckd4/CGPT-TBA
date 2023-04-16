from logger import logger
from dotenv import load_dotenv

import os


class Bot:
	def __init__(self):
		load_dotenv()
		logger.debug("Reading environment variables")
		self.bot_token = os.getenv("TELEGR_TOKEN")
		self.oai_token = os.getenv("OPENAI_TOKEN")
		logger.info("Bot configuration")
		logger.debug(f"Telegram token: {self.bot_token}")
		logger.debug(f"OpenAI token: {self.oai_token}")

	def start(self):
		logger.info("Bot started")
