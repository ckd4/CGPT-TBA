import logging
import datetime

logger = logging.getLogger("tg")

def configure() -> None:
	logger.setLevel(logging.DEBUG)
	console_handler = logging.StreamHandler()
	console_handler.setLevel(logging.DEBUG)
	console_handler.setFormatter(ConsoleFormatter())
	logger.addHandler(console_handler)
	logger.debug("CONSOLE DEBUG HANDLER CONFIGURATED")
	file_handler = logging.FileHandler("logs\\" + datetime.datetime.now().strftime("%d%m%Y%H%M%S.log"))
	file_handler.setLevel(logging.DEBUG)
	file_handler.setFormatter(FileFormatter())
	logger.addHandler(file_handler)
	logger.debug("FILE DEBUG HANDLER CONFIGURATED")
	logger.info("LOGGER CONFIGURATED")

class FileFormatter(logging.Formatter):

	FORMATS = {
		logging.DEBUG: "[ D ] %(asctime)s | %(message)s",
		logging.INFO: "[ I ] %(asctime)s | %(message)s",
		logging.WARNING: "[ W ] %(asctime)s | %(message)s: (%(filename)s:%(lineno)d)",
		logging.ERROR: "[ E ] %(asctime)s | %(message)s: (%(filename)s:%(lineno)d)",
		logging.CRITICAL: "[ C ] %(asctime)s | %(message)s: (%(filename)s:%(lineno)d)"
	}

	def format(self, record):
		log_fmt = self.FORMATS.get(record.levelno)
		formatter = logging.Formatter(log_fmt, datefmt="%m/%d/%Y %I:%M:%S")
		return formatter.format(record)

class ConsoleFormatter(logging.Formatter):
	debug = "\x1b[96;20m"
	info = "\x1b[32;20m"
	warning = "\x1b[33;20m"
	error = "\x1b[91;20m"
	critical = "\x1b[31;20m"
	reset = "\x1b[0m"

	FORMATS = {
		logging.DEBUG: debug + "%(asctime)s | %(message)s" + reset,
		logging.INFO: info + "%(asctime)s | %(message)s" + reset,
		logging.WARNING: warning + "%(asctime)s | %(message)s: (%(filename)s:%(lineno)d)" + reset,
		logging.ERROR: error + "%(asctime)s | %(message)s: (%(filename)s:%(lineno)d)" + reset,
		logging.CRITICAL: critical + "%(asctime)s | %(message)s: (%(filename)s:%(lineno)d)" + reset
	}

	def format(self, record):
		log_fmt = self.FORMATS.get(record.levelno)
		formatter = logging.Formatter(log_fmt, datefmt="%m/%d/%Y %I:%M:%S")
		return formatter.format(record)
