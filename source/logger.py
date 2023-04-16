import console_format
import file_format
import logging
import datetime

logger = logging.getLogger("tg")

def configure() -> None:
	logger.setLevel(logging.DEBUG)
	console_handler = logging.StreamHandler()
	console_handler.setLevel(logging.DEBUG)
	console_handler.setFormatter(console_format.ConsoleFormatter())
	logger.addHandler(console_handler)
	logger.debug("CONSOLE DEBUG HANDLER CONFIGURATED")
	file_handler = logging.FileHandler("logs\\" + datetime.datetime.now().strftime("%d%m%Y%H%M%S.log"))
	file_handler.setLevel(logging.DEBUG)
	file_handler.setFormatter(file_format.FileFormatter())
	logger.addHandler(file_handler)
	logger.debug("FILE DEBUG HANDLER CONFIGURATED")
	logger.info("LOGGER CONFIGURATED")
