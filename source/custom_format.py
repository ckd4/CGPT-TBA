import logging

class CustomFormatter(logging.Formatter):
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
