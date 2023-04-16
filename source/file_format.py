import logging

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
