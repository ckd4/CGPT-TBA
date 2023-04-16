import custom_format
import logging

logger = logging.getLogger("tg")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(custom_format.CustomFormatter())
logger.addHandler(ch)

logger.info("dxdxdxd")
logger.debug("dxdxdxd")
logger.warning("dxdxdxd")
logger.error("dxdxdxd")
logger.critical("dxdxdxd")
