import logging
from flask import url_for
from logging.handlers import RotatingFileHandler

# info logger
info_logger = logging.getLogger('info_logger')
info_logger.setLevel(logging.INFO)
info_file_handler = RotatingFileHandler('Door-Lock-with-Passcode-from-Phone/project/static/logs/info.log', maxBytes=10000, backupCount=5)

# error logger
error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
error_file_handler = RotatingFileHandler('Door-Lock-with-Passcode-from-Phone/project/static/logs/error.log', maxBytes=10000, backupCount=5)

# log message format
log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

info_file_handler.setFormatter(log_formatter)
error_file_handler.setFormatter(log_formatter)

info_logger.addHandler(info_file_handler)
error_logger.addHandler(error_file_handler)
