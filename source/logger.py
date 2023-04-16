import custom_format
import logging

logger = logging.getLogger("tg")

def configure() -> None:
	logger.setLevel(logging.DEBUG)
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	ch.setFormatter(custom_format.CustomFormatter())
	logger.addHandler(ch)
	logger.info("Logger configurated")
