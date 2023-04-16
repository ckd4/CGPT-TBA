import logging

class CustomFormatter(logging.Formatter):
	debug = "\x1b[96;20m"
	info = "\x1b[38;20m"
	warning = "\x1b[33;20m"
	error = "\x1b[91;20m"
	critical = "\x1b[31;20m"
	reset = "\x1b[0m"
	format = "%(asctime)s | %(message)s: (%(filename)s:%(lineno)d)"

	FORMATS = {
		logging.DEBUG: debug + format + reset,
		logging.INFO: info + format + reset,
		logging.WARNING: warning + format + reset,
		logging.ERROR: error + format + reset,
		logging.CRITICAL: critical + format + reset
	}

	def format(self, record):
		log_fmt = self.FORMATS.get(record.levelno)
		formatter = logging.Formatter(log_fmt, datefmt="%m/%d/%Y %I:%M:%S")
		return formatter.format(record)
