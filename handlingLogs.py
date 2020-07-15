import logging

logging.basicConfig(filename="scriptLogs.log",
                    format="%(asctime)s:%(levelname)s:%(message)s",
                    datefmt="%m/%d/%y")

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("this is debug logger")
logger.info(" this is info logger")
logger.warning(" this is warning logger")
logger.exception("this is exception logger")
logger.error("this is error logger")
logger.critical(" **** this is critical logger *********")
